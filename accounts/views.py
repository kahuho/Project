from django.shortcuts import render
from django.views.generic import  TemplateView

# Create your views here.
from django.shortcuts import render, redirect
from django.http import request
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Profile
from sell.models import Products


def user_login(request):
    # form = LoginForm(request.POST or None)
    if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
                # where the user exists in the database
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, 'Invalid Login')

                return redirect('login')

    else:
        return render(request, 'accounts/registration/login.html'   )



class HomeView(TemplateView):
    template_name = "accounts/home.html"



def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST or None)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            profile= Profile.objects.create(user=new_user)

            return render(request, 'accounts/registration/login.html', {'new_user': new_user})
    else:
         user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})
def logout(request):
    return  redirect('home')


# Create your views here.
@login_required
def edit (request):


    if request.method == 'POST':
        user_form = UserEditForm(instance= request.user, data = request.POST)
        profile_form = ProfileEditForm (instance = request.user.profile, data = request.POST, files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
        else:
            messages.error (request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
        return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def viewProfile(request):
    if request.method == 'POST':
        form = ProfileEditForm
