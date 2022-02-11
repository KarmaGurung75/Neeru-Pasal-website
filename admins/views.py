from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from homepages.models import ProductCategory, ProductList, FileUpload, SendFeedback, Order
from .forms import CreateUserForm
from django.contrib import messages

@login_required
@admin_only
def admin_dashboard(request):
    category = ProductCategory.objects.all()
    category_count = category.count()
    list = ProductList.objects.all()
    list_count = list.count()
    gallery = FileUpload.objects.all()
    gallery_count = gallery.count()
    sendFeedback = SendFeedback.objects.all()
    sendFeedback_count = sendFeedback.count()
    order = Order.objects.all()
    order_count = order.count()
    user = User.objects.filter(is_staff=0)
    user_count = user.count()
    admin = User.objects.filter(is_staff=1)
    admin_count = admin.count()

    context= {
        'category': category_count,
        'list': list_count,
        'gallery': gallery_count,
        'sendFeedback': sendFeedback_count,
        'user': user_count,
        'admin': admin_count,
        'order': order_count,
    }
    return render(request, 'admins/homepage.html', context)

@login_required
@admin_only
def show_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users': users
    }
    return render(request, 'admins/users.html', context)

@login_required
@admin_only
def show_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'admins': admins
    }
    return render(request, 'admins/admins.html', context)

@login_required
@admin_only
def promote_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Promoted To Admin')
    return redirect('/admins/admins')

@login_required
@admin_only
def demote_admin(request, user_id):
    admin = User.objects.get(id=user_id)
    admin.is_staff = False
    admin.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Demoted To User')
    return redirect('/admins/users')

@login_required
@admin_only
def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User Registered Successfully")
            return redirect('/users')
        else:
            messages.add_message(request, messages.ERROR, "Unable To Register User")
            return render(request, 'admins/adduser.html', {'form_register': form})
    context = {
        'form_register': CreateUserForm,
    }
    return render(request, 'admins/adduser.html', context)