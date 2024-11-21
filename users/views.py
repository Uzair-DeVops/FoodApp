from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            # Add a success message
            messages.success(request, f"Welcome {user_name}, your account has been created successfully!")
            return redirect('food:index')  # Redirect to the index page
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")  # Add this
    return redirect('food:index')  # Ensure this redirects to the page containing the alert
  # Adjust the redirect URL as needed
from django.shortcuts import render

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')



from django.contrib import messages

from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Store username in session
                request.session['username'] = username
                messages.success(request, f"Welcome back, {username}!")  # Add this
                return redirect('food:index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()
    
    return render(request, 'users/login.html', {'form': form})
