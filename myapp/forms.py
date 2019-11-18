from django import forms
from django.contrib.auth.models import User
from myapp.models import SiteConfiguration,SmtpConfiguration
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class LoginForm(forms.ModelForm):
    username=forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput,max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'password']


class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(required=True)
    new_password1 = forms.CharField(required=True)
    new_password2 = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super(PasswordChangedForm, self).clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError('The passwords does not match.')
        return cleaned_data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class SiteForm(forms.ModelForm):
    site_name = forms.CharField(max_length=50, required=True)
    site_email=forms.EmailField(max_length=50, required=True)
    site_favicon = forms.ImageField(required=True)
    site_logo = forms.ImageField(required=True)
    site_address = forms.CharField(max_length=200,required=True)
    copy_right = forms.CharField(max_length=200,required=True)

    class Meta:
        model = SiteConfiguration
        fields = ['site_name', 'site_email', 'site_favicon','site_logo','site_address','copy_right']


class SmtpForm(forms.ModelForm):
    smtp_email=forms.EmailField(max_length=50, required=True)
    smtp_password = forms.CharField(widget=forms.PasswordInput,max_length=50, required=True)

    class Meta:
        model = SmtpConfiguration
        fields = ['smtp_email', 'smtp_password']