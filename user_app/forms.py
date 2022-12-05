from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                      'placeholder': "Username"}))

    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                     'placeholder': "Email"}))

    password1 = forms.CharField(label='', widget=(forms.PasswordInput(attrs={'class': "form-field",
                                                                             'placeholder': "Password"})))

    password2 = forms.CharField(label='', widget=(forms.PasswordInput(attrs={'class': "form-field",
                                                                             'placeholder': "Password Confirmation"})))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'password': None
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                      'placeholder': "Login"}))

    password = forms.CharField(label='', widget=(forms.PasswordInput(attrs={'class': "form-field",
                                                                            'placeholder': "Password"})))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password")
        help_texts = {
            'password': None
        }
