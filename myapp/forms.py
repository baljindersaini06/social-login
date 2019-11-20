from django import forms
from django.contrib.auth.models import User
from myapp.models import SiteConfiguration,SmtpConfiguration
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput,max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'password']


class PasswordChangedForm(PasswordChangeForm):
    old_password_flag = True
    old_password = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True)
    new_password1 = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True)
    new_password2 = forms.CharField(widget=forms.PasswordInput,max_length=30,required=True)

    def set_old_password_flag(self): 

    #This method is called if the old password entered by user does not match the password in the database, which sets the flag to False

        self.old_password_flag = False

        return 0

    def clean_old_password(self, *args, **kwargs):
        old_password = self.cleaned_data.get('old_password')

        if not old_password:
            raise forms.ValidationError("You must enter your old password.")

        if self.old_password_flag == False:
        #It raise the validation error that password entered by user does not match the actucal old password.

            raise forms.ValidationError("The old password that you have entered is wrong.")

        return old_password


    def clean(self):
        cleaned_data = super(PasswordChangedForm, self).clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError('The passwords does not match.')
        return cleaned_data


class UserForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ImageForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['profile_image']
        


class SiteForm(forms.ModelForm):
    site_name = forms.CharField(max_length=50, required=True)
    site_email=forms.EmailField(max_length=50, required=True)
    site_favicon = forms.ImageField()
    site_logo = forms.ImageField()
    site_address = forms.CharField(max_length=200,required=True)
    copy_right = forms.CharField(max_length=200,required=True)
    
    class Meta:
        model = SiteConfiguration
        fields = ['site_name', 'site_email', 'site_favicon','site_logo','site_address','copy_right']


class UpdateSiteForm(forms.ModelForm):
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

