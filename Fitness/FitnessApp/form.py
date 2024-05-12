from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile

class UserProfileForm(UserCreationForm):
    name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(max_length=254, required=True)
    age = forms.IntegerField(required=True)
    weight = forms.FloatField(required=True)
    height = forms.FloatField(required=True)
    subscription = forms.DateTimeField(required=True)
    #picture = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ("username", "name", "email", "age", "weight", "height", "subscription", "password1", "password2")
        labels = {
            'username': 'Username:',
            'password1': 'Password:',
            'password2': 'Confirm Password:',
        }
        help_texts = {
            'username': 'Enter a unique username.',
            'password1': 'Your password should be at least 8 characters long.',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise ValidationError("Name cannot contain numbers.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered.")
        return email


    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = UserProfile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                email=self.cleaned_data['email'],
                age=self.cleaned_data['age'],
                weight=self.cleaned_data['weight'],
                height=self.cleaned_data['height'],
                subscription=self.cleaned_data['subscription'],
                #picture=self.cleaned_data.get('picture')
            )
        return user

