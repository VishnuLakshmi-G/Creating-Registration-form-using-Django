from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            username = user.username  # Extract the username
            return redirect('success', username=username)  # Redirect to success page with the username
        else:
            return render(request, 'signup.html', {'form': form})  # Re-render form with error messages
    else:
        form = UserRegistrationForm()  # Create an empty form on GET request

    return render(request, 'signup.html', {'form': form})  # Render form template

def success(request, username):
    return render(request, 'success.html', {'username': username})  # Render success template with username