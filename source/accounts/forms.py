from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.core.exceptions import ValidationError

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save(commit=commit)
        Profile.objects.create(user=user)
        return user

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        email = cleaned_data.get('email')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name:
            if not last_name:
                errors.append(ValidationError('Заполните хотя бы одно из двух полей!'))
        if not email:
            errors.append(ValidationError('Введите Email'))
        if errors:
            raise ValidationError(errors)
        return cleaned_data


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


