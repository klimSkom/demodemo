from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Zayavka

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CreateZayavkaForm(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = ['type', 'datetime', 'payment']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }