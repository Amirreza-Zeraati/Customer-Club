from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ["username", "phone", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        phone = self.cleaned_data['phone']
        Profile.objects.update_or_create(user=user, defaults={'phone': phone})
        return user