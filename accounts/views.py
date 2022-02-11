from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, CreateUserForm, ProfileForm
from .models import Profile
from homepages.models import Cart, Wishlist
from django.contrib.auth import update_session_auth_hash

def homepage(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    context = {
        'activate_home': 'active',
        'count': cart_count,
        'count_list': wishlist_count,
    }
    return render(request, 'accounts/homepage.html', context)

def logout_user(request):
    logout(request)
    return redirect('/login')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    return redirect('/')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/admins')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Username Or Password')
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)
            messages.add_message(request, messages.SUCCESS, "User Registered Successfully")
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, "Unable To Register User")
            return render(request, 'accounts/register.html', {'form_register': form})
    context = {
        'form_register': CreateUserForm,
    }
    return render(request, 'accounts/register.html', context)


def profile(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    profile = request.user.profile
    context = {
        'form': ProfileForm(profile),
        'activate_profile': 'active',
        'count': cart_count,
        'count_list': wishlist_count,
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile Updated Successfully")
            return redirect('/my_profile')
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active',
        'count': cart_count,
        'count_list': wishlist_count,
    }
    return render(request, 'accounts/editprofile.html', context)


def change_password(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password Changed Successfully")
            return redirect('/my_profile')
        else:
            messages.add_message(request, messages.ERROR, "Please Verify The Form Fields")
            return render(request, 'accounts/password_change.html', {'password_change_form': form})
    context = {
        'password_change_form': PasswordChangeForm(request.user),
        'count': cart_count,
        'count_list': wishlist_count,

    }
    return render(request, 'accounts/password_change.html', context)
