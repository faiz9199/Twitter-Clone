from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content','media']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What’s happening?'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']