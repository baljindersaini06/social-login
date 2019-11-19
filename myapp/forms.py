from django import forms
from django.contrib.auth.models import User
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



class UserForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'profile_image']

class ImageForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['profile_image']
