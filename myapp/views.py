from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import UserCreateForm, LoginForm, PasswordChangedForm, UserForm,SmtpForm,SiteForm, ImageForm,UpdateSiteForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
User = get_user_model()
from myapp.models import SiteConfiguration,SmtpConfiguration

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

# def user_update(request):
#     return render(request, 'myapp/profile.html')

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
    password_form = PasswordChangedForm(request.POST)
    profile_form = UserForm(request.POST)
    image_form = ImageForm(request.POST)
    site_form = SiteForm()
    smtp_form = SmtpForm()

    try:
        updatesite_form=SiteConfiguration.objects.get(user=request.user) 
    except SiteConfiguration.DoesNotExist:
        updatesite_form = None

    try:
        smtp_set=SmtpConfiguration.objects.get(user=request.user)
    except SmtpConfiguration.DoesNotExist:
        smtp_set = None
   
   
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        if 'btnform2' in request.POST:
            password_form = PasswordChangedForm(request.user, request.POST)
            if request.POST.get("old_password"):
                user = User.objects.get(username= request.user.username)
                if user.check_password('{}'.format(old_password)) == False:
                    password_form.set_old_password_flag()
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return HttpResponseRedirect(reverse('profile_account'))
            else:
                messages.error(request, 'Please correct the error below.')
        elif 'btnform1' in request.POST:
            profile_form = UserForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
        elif 'btnform3' in request.POST:
            image_form = ImageForm(request.POST, request.FILES , instance=request.user)
            if (image_form.is_valid()):
                image_form.save()            
                return HttpResponseRedirect(reverse('profile_account'))
        elif 'btnform4' in request.POST:
            if SiteConfiguration.objects.filter(user=request.user).exists():

                try:
                    site_sett=SiteConfiguration.objects.get(user=request.user) 
                except SiteConfiguration.DoesNotExist:
                    site_sett = None

                updatesite_form = UpdateSiteForm(request.POST, request.FILES , instance=site_sett)        
                if updatesite_form.is_valid():
                    updatesite_form.save()            
                    return HttpResponseRedirect(reverse('profile_account'))                     
            else:       
                site_form = SiteForm(request.POST, request.FILES)
                if site_form.is_valid():
                    post = site_form.save(commit=False)
                    post.user = request.user
                    post.save()  
                    messages.success(request, 'Your site settings are successfully added !')
                    return HttpResponseRedirect(reverse('profile_account'))  
    
        elif 'btnform5' in request.POST:
            if SmtpConfiguration.objects.filter(user=request.user).exists():

                try:
                    smtp_sett=SmtpConfiguration.objects.get(user=request.user)
                except SmtpConfiguration.DoesNotExist:
                    smtp_sett = None      

                smtp_form = SmtpForm(request.POST, request.FILES , instance=smtp_sett)        
                if smtp_form.is_valid():
                    smtp_form.save()            
                    return HttpResponseRedirect(reverse('profile_account'))                      
            else:       
                smtp_form = SmtpForm(request.POST, request.FILES)
                if smtp_form.is_valid():
                    smtp_post = smtp_form.save(commit=False)
                    smtp_post.user = request.user
                    smtp_post.save()  
                    messages.success(request, 'Your smtp settings are successfully added !')
                    return HttpResponseRedirect(reverse('profile_account'))     
        else:
            raise Http404
    else:
        if SiteConfiguration.objects.filter(user=request.user).exists():
            site_profile_form = SiteForm(instance=SiteConfiguration.objects.get(user=request.user)) 
        elif SmtpConfiguration.objects.filter(user=request.user).exists():
            smtp_form = SmtpForm(instance=SmtpConfiguration.objects.get(user=request.user)) 

    return TemplateResponse(request, template="myapp/extra_profile_account.html", context={
        'password_form': password_form,
        'profile_form': profile_form,
        'site_form': site_form,
        'smtp_form': smtp_form,
        'image_form': image_form,
       
        'smtp_set':smtp_set,
        'updatesite_form':updatesite_form,
    })

# def siteupdate(request):
#     if Site.objects.filter(user=username).exists():
#     if request.method == 'POST':
#         site_profile_form = UpdateSiteForm(request.POST, request.FILES , instance=request.user.site)
        
#         if site_profile_form.is_valid():
           
#             site_profile_form.save()            
#             return HttpResponseRedirect(reverse('success'))
        
#     else:
#         site_profile_form = UpdateSiteForm(instance=request.user)
#     return render(request, 'profile_tabs/updatesite.html', {
#         'site_profile_form': site_profile_form,
       
#     })

def test(request):
  response_str = "false"
  if request.is_ajax():
    old_password = request.GET.get("old_password")
    request_user = User.objects.get(id=request.user.id)
    if(request_user.check_password(old_password) == True):
        response_str = "true"
    return HttpResponse(response_str)





# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = ImageForm(request.POST, request.FILES , instance=request.user)
        
#         if (user_form.is_valid()):
           
#             user_form.save()            
#             return HttpResponseRedirect(reverse('profile_account'))
        
#     else:
#         user_form = ImageForm(instance=request.user)
#     return render(request, 'profile_tabs/change_avtar.html', {
#         'user_form': user_form
#     })



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



