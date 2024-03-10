# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login

from .models import User





# views.py

from django.shortcuts import render, redirect
from .models import User  # Assuming you have a User model

def home(request):
    return render(request, 'navbar.html')
def navbar(request):
    return render(request, 'navbar.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'User does not exist.')  # Display error message if user does not exist
            return render(request, 'login.html')  # Render the login page again
    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Create a new user instance and save it to the database
            user = User.objects.create(first_name=firstname, last_name=lastname, username=username, password=password)
            user.save()
            return redirect('login')  # Redirect to login page
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

    return render(request, 'register.html')
