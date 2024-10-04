from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")  # Secure password field

    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']