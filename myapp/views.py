from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import UserCreateForm, LoginForm, PasswordChangedForm, UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.template.response import TemplateResponse


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            return redirect('dashboard')

    else:
        form = UserCreateForm()
    return render(request, 'auth/user_form.html', {'form': form})

@login_required
def index(request):
    return render(request, 'myapp/index.html')


@login_required
def profile(request):
    return render(request, 'myapp/profile.html')


# def profile_account(request):
#     return render(request, 'myapp/extra_profile_account.html')


@login_required
def calender(request):
    return render(request, 'myapp/page_calender.html')

def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)          
            if user is not None:
                if user.is_active:
                    login(request, user)    
                    return redirect('dashboard')
                    
    else:
        login_form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': login_form,})


def success(request):
    return render(request, 'myapp/success.html')


@login_required
def profile_account(request):
    password_form = PasswordChangedForm(request.POST, prefix='password')
    profile_form = UserForm(request.POST,prefix='profile')

    if request.method == "POST":
        if 'password-btnform2' in request.POST:
            password_form = PasswordChangedForm(request.user, request.POST, prefix='password')
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile_account')
            else:
                messages.error(request, 'Please correct the error below.')
        elif 'profile-btnform1' in request.POST:
            profile_form = UserForm(request.POST, instance=request.user, prefix='profile')
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile_account')
        else:
            raise Http404

    return TemplateResponse(request, template="myapp/extra_profile_account.html", context={
        'password_form': password_form,
        'profile_form': profile_form,
    })


# def change_password(request):
#     #print("helloooooo")
#     if request.method == 'POST':
#         form = PasswordChangedForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('profile_account')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangedForm(request.user)
#     return render(request, 'myapp/extra_profile_account.html', {'form': form})


# @login_required
# def edit_names(request):
#     args = {}
#     if request.method == "POST":
#         form = UserForm(data=request.POST, instance=request.user)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return HttpResponseRedirect(reverse('profile_account'))
#     else:
#         form = UserForm(instance=request.user)
#         args['form'] = form
#         return render(request, 'myapp/extra_profile_account.html', args)


# @login_required
# def user_update(request, template_name='myapp/extra_profile_account.html'):
#     # user= get_object_or_404(User)
#     print("Helloo")
#     fform = UserForm(request.POST, instance=request.user)
#     if fform.is_valid():
#         fform.save()
#         return redirect('profile_account')
#     return render(request, template_name, {'fform':fform})