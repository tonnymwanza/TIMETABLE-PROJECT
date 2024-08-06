from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.views import View
from django.contrib import messages
# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')

# the view user registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'the username is already taken. try another one')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'the email is already in use. pick a different one')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                return redirect('login')
        else:
            messages.error(request, 'the passwords dont match. try again')
    return render(request, 'register.html')

# the user login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'the login details are invalid. try again')
    return render(request, 'login.html')