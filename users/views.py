from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'Password and Confirm Password do not match!')
            return redirect('/users/register')
        
        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'User already exists!')
            return redirect('/users/register')
        try:
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('/users/login')
        except:
            messages.add_message(request, constants.ERROR, 'Server internal error!')
            return redirect('/users/register')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logged in!')
            return redirect('/flashcard/new_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'Invalid Username or Password!')
            return redirect('/users/login/')
        
def logout(request):
    auth.logout(request)
    return redirect('/users/login')