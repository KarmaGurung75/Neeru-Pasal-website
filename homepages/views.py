from django.shortcuts import render, redirect
import requests as req

from .models import FileUpload, SendFeedback, ProductList, ProductCategory, Cart, Order, Wishlist
from .forms import FileForm, FeedbackForm, ProductCategoryForm, ProductListForm, OrderForm
from django.http import HttpResponse
import os
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only, admin_only
from .filters import ProductFilter


# =====================About Us Part========================================
def about(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    context = {
        'activate_about': 'active',
        'count': cart_count,
        'count_list': wishlist_count
    }
    return render(request, 'homepages/about.html', context)


# =====================Category Part========================================
@login_required
@admin_only
def productcategory_form(request):
    if request.method == "POST":
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product Category Added Successfully')
            return redirect("/homepages/get_product_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Add Product Category')
            return render(request, 'homepages/productcategory_form.html', {'product_category_form': form})
    context = {
        'product_category_form': ProductCategoryForm,
        'activate_productcategory': 'active'
    }
    return render(request, 'homepages/productcategory_form.html', context)


@login_required
@admin_only
def get_productcategory(request):
    product_categories = ProductCategory.objects.all().order_by('-id')
    context = {
        'get_product_category': product_categories,
        'activate_productcategory': 'active'
    }
    return render(request, 'homepages/getproductcategory.html', context)


@login_required
@admin_only
def delete_productcategory(request, productcategory_id):
    product_categories = ProductCategory.objects.get(id=productcategory_id)
    os.remove(product_categories.category_image.path)
    product_categories.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted Successfully')

    return redirect('/homepages/get_product_category')


@login_required
@admin_only
def update_productcategory(request, productcategory_id):
    product_catgory = ProductCategory.objects.get(id=productcategory_id)
    if request.method == "POST":
        form = ProductCategoryForm(request.POST, request.FILES, instance=product_catgory)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product Category Updated Successfully')
            return redirect("/homepages/get_product_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Update Product Category')
            return render(request, 'homepages/update_product_category.html', {'product_category_form': form})
    context = {
        'product_category_form': ProductCategoryForm(instance=product_catgory),
        'activate_productcategory': 'active'
    }
    return render(request, 'homepages/update_product_category.html', context)


@user_only
def show_product_category(request):
    product_category = ProductCategory.objects.all().order_by('-id')
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    context = {
        'product_category': product_category,
        'activate_list': 'active',              #-------
        'count': cart_count,
        'count_list': wishlist_count
    }
    return render(request, 'homepages/product.html', context)


# ===================== Product List Part========================================
@login_required
@admin_only
def productlist_form(request):
    if request.method == "POST":
        form = ProductListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product List Added Successfully')
            return redirect("/homepages/get_product_list")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Add Product List')
            return render(request, 'homepages/productlist_form.html', {'product_list_form': form})
    context = {
        'product_list_form': ProductListForm,
        'activate_productlist': 'active'
    }
    return render(request, 'homepages/productlist_form.html', context)


@login_required
@admin_only
def get_productlist(request):
    product_list = ProductList.objects.all().order_by('-id')
    product_list_filter = ProductFilter(request.GET, queryset=product_list)
    product_list_filter_final = product_list_filter.qs
    context = {
        'filter':product_list_filter,
        'get_product_list': product_list_filter_final,
        'activate_productcategory': 'active'
    }
    return render(request, 'homepages/getproductlist.html', context)


@login_required
@admin_only
def delete_productlist(request, productlist_id):
    product_list = ProductList.objects.get(id=productlist_id)
    os.remove(product_list.product_image.path)
    product_list.delete()
    messages.add_message(request, messages.SUCCESS, 'Product List Deleted Successfully')

    return redirect('/homepages/get_product_list')


@login_required
@admin_only
def update_productlist(request, productlist_id):
    product_list = ProductList.objects.get(id=productlist_id)
    if request.method == "POST":
        form = ProductListForm(request.POST, request.FILES, instance=product_list)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product List Updated Successfully')
            return redirect("/homepages/get_product_list")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Update Product List')
            return render(request, 'homepages/update_product_list.html', {'product_list_form': form})
    context = {
        'product_list_form': ProductListForm(instance=product_list),
        'activate_productlist': 'active'
    }
    return render(request, 'homepages/update_product_list.html', context)


@user_only
def show_list(request, productcategory_id):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    product_list = ProductCategory.objects.get(id=productcategory_id)
    context = {
        'product_list': product_list,
        'activate_list': 'active',
        'count': cart_count,
        'count_list': wishlist_count
    }
    return render(request, 'homepages/product_list.html', context)


# =====================Gallery Admin Part========================================
# To show the added photos in admin pannel.
@login_required
@admin_only
def gallery_modelform(request):
    files = FileUpload.objects.all().order_by('-id')
    context = {
        'files': files,
    }
    return render(request, 'homepages/gallery_modelform.html', context)


# Function that adds the photos.
@login_required
@admin_only
def add_gallery_modelform(request):
    form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/homepages/gallery_modelform")
        else:
            return HttpResponse("!!!Unable To Add Photo!!!")
    context = {
        'file_form': form,
    }
    return render(request, 'homepages/add_gallery_modelform.html', context)


# Function that helps to delete the photos from gallery.
@login_required
@admin_only
def delete_gallery_modelform(request, file_id):
    image = FileUpload.objects.get(id=file_id)
    os.remove(image.file.path)
    image.delete()
    return redirect('/homepage/gallery_modelform')


# Function that helps to edit the photos from gallery.
@login_required
@admin_only
def update_gallery_modelform(request, file_id):
    image = FileUpload.objects.get(id=file_id)
    if request.method == "POST":
        if request.FILES.get('file'):
            os.remove(image.file.path)
        form = FileForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect("/homepages/gallery_modelform")
        else:
            return HttpResponse("!!!Unable To Update File!!!")
    context = {
        'file_form': FileForm(instance=image),
    }
    return render(request, 'homepages/update_gallery_modelform.html', context)


# =====================Gallery User Part========================================
# Function that helps to display the images in the gallery in user form.
def show_gallery(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    gallery = FileUpload.objects.all().order_by('-id')
    context = {
        'activate_gallery': 'active',
        'gallery': gallery,
        'count': cart_count,
        'count_list': wishlist_count
    }
    return render(request, 'homepages/gallery.html', context)


# =====================Contact Us Part========================================
def contact(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
            Name: {} {}
            
            New Message: {}
            
            From: {}
        '''.format(data['firstname'], data['lastname'], data['message'], data['email'])
        send_mail(data['subject'], message, '', ['karma1661@gmail.com'])
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Message sent successfully')
            return redirect('/homepages/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to Send Feedback')
            return render(request, 'homepages/contact.html', {'form_message': form})

    context = {
        'form_feedback': FeedbackForm,
        'activate_contact': 'active',
        'count': cart_count,
        'count_list': wishlist_count
    }
    return render(request, 'homepages/contact.html', context)


@login_required
@admin_only
def get_feedback(request):
    feedback = SendFeedback.objects.all().order_by('-id')
    context = {
        'feedback': feedback,
        'activate_message': 'active',

    }
    return render(request, 'homepages/get_feedback.html', context)


@login_required
@admin_only
def delete_feedback(request, feedback_id):
    feedback = SendFeedback.objects.get(id=feedback_id)
    feedback.delete()
    messages.add_message(request, messages.SUCCESS, 'Feedback Deleted successfully')
    return redirect('/homepages/get_feedback')


# =================================Add To Cart==================================================
@login_required
@user_only
def add_to_cart(request, productlist_id):
    user = request.user
    product = ProductList.objects.get(id=productlist_id)
    check_item_presence = Cart.objects.filter(user=user, product=product)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Item Is Already In The Cart.')
        return redirect("/homepages/mycart")

    else:
        cart = Cart.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Product Added To Cart')
            return redirect("/homepages/mycart")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Add Product To Cart')


@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    context = {
        'items': items,
        'activate_my_cart': 'active',
        'count': cart_count,
        'count_list': wishlist_count
    }
    return render(request, 'homepages/mycart.html', context)


@login_required
@user_only
def remove_cart_item(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Product Removed Successfully')
    return redirect('/homepages/mycart')


# =================================WishList==================================================
@login_required
@user_only
def add_wishlist(request, productlist_id):
    user = request.user
    product = ProductList.objects.get(id=productlist_id)
    check_item_presence = Wishlist.objects.filter(user=user, product=product)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Item Is Already In The Wishlist.')
        return redirect("/homepages/mywishlist")

    else:
        cart = Wishlist.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Product Added To Wishlist')
            return redirect("/homepages/mywishlist")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Add Product To Wishlist')


@login_required
@user_only
def show_mywishlist(request):
    user = request.user
    items = Wishlist.objects.filter(user=user)
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    context = {
        'items': items,
        'activate_my_wishlist': 'active',
        'count': cart_count,
        'count_list': wishlist_count,
    }
    return render(request, 'homepages/mywishlist.html', context)


@login_required
@user_only
def remove_wishlist(request, wishlist_id):
    item = Wishlist.objects.get(id=wishlist_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Wishlist Product Removed Successfully')
    return redirect('/homepages/mywishlist')


# =============================================Order=====================================================
@login_required
@user_only
def order_form(request, productlist_id, cart_id):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    user = request.user
    product = ProductList.objects.get(id=productlist_id)
    cart_item = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = product.product_price
            total_price = int(quantity) * int(price)
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')
            payment_method = request.POST.get('payment_method')
            order = Order.objects.create(product=product,
                                         user=user,
                                         quantity=quantity,
                                         total_price=total_price,
                                         contact_no=contact_no,
                                         contact_address=contact_address,
                                         status="Pending",
                                         payment_method=payment_method,
                                         payment_status=False
                                         )
            if order:
                # messages.add_message(request, messages.SUCCESS, 'Item Ordered. Continue Payment for Verification')
                # cart_item.delete()
                context = {
                    'order': order,
                    'cart': cart_item,
                    'count': cart_count,
                    'count_list': wishlist_count,
                }
                return render(request, 'homepages/esewa_payment.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'homepages/order_form.html', {'order_form': form})
    context = {
        'order_form': OrderForm
    }
    return render(request, 'homepages/order_form.html', context)


import requests as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get("oid")
    amount = request.GET.get("amt")
    refId = request.GET.get("refId")
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/homepages/mycart')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/homepages/mycart')


def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/homepages/mycart')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/homepages/mycart')


@login_required
@user_only
def my_order(request):
    cart = Cart.objects.all()
    cart_count = cart.count()
    wishlist = Wishlist.objects.all()
    wishlist_count = wishlist.count()
    user = request.user
    items = Order.objects.filter(user=user, payment_status=True).order_by('-id')
    context = {
        'items': items,
        'activate_myorders': 'active',
        'count': cart_count,
        'count_list': wishlist_count,

    }
    return render(request, 'homepages/my_order.html', context)


@login_required
@admin_only
def get_order(request):
    order = Order.objects.all().order_by('-id')
    context = {
        'order': order,
        'activate_order': 'active',
    }
    return render(request, 'homepages/get_order.html', context)

@login_required
@admin_only
def deleteOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    messages.add_message(request, messages.SUCCESS, 'Order has been deleted Successfully')
    return redirect('/homepages/get_order')

@login_required
@admin_only
def updateOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Delivered'
    order.save()
    messages.add_message(request, messages.SUCCESS, 'Order Has Been Delivered Successfully')
    return redirect('/homepages/get_order')