from django.urls import path
from . import views

urlpatterns = [
    # About Us Page Path
    path('about_us', views.about, name='about'),
    # Product Category Page Path Admin Part
    path('product_category_form', views.productcategory_form),
    path('get_product_category', views.get_productcategory),
    path('delete_product_category/<int:productcategory_id>', views.delete_productcategory),
    path('update_product_category/<int:productcategory_id>', views.update_productcategory),
    # Product Category Page Path User Part
    path('list', views.show_product_category),
    # Product List Page Path Admin Part
    path('product_list_form', views.productlist_form),
    path('get_product_list', views.get_productlist),
    path('delete_product_list/<int:productlist_id>', views.delete_productlist),
    path('update_product_list/<int:productlist_id>', views.update_productlist),
    # Product List Page Path User Part
    path('show_list/<int:productcategory_id>', views.show_list, name='show_list'),
    # Gallery Page Path Admin Part
    path('gallery_modelform', views.gallery_modelform),
    path('add_gallery_modelform', views.add_gallery_modelform),
    path('delete_gallery_modelform/<int:file_id>', views.delete_gallery_modelform, name="delete_gallery_modelform"),
    path('update_gallery_modelform/<int:file_id>', views.update_gallery_modelform),
    # Gallery Page Path User Part
    path('gallery', views.show_gallery, name='show_gallery'),
    # Contact Us Page Path User Part
    path('contact', views.contact, name='contact'),
    # Contact Us Page Path Admin Part
    path('get_feedback', views.get_feedback),
    path('delete_feedback/<int:feedback_id>', views.delete_feedback),
    # Add To Cart Page Path User Part
    path('add_to_cart/<int:productlist_id>', views.add_to_cart),
    path('mycart', views.show_cart_items, name='show_cart_items'),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    # Wishlist Page Path User Part
    path('add_wishlist/<int:productlist_id>', views.add_wishlist),
    path('mywishlist', views.show_mywishlist, name='my_wishlist'),
    path('remove_wishlist/<int:wishlist_id>', views.remove_wishlist),
    # Order Form Product Page Path User Part
    path('order_form/<int:productlist_id>/<int:cart_id>', views.order_form),
    # Esewa Page Path User Part
    path('esewa_verify', views.esewa_verify),
    # Order Product Page Path User Part
    path('my_order', views.my_order, name='my_order'),
    # Order Product Page Path Admin Part
    path('get_order', views.get_order),
    path('deleteOrder/<int:order_id>', views.deleteOrder),
    path('updateOrder/<int:order_id>', views.updateOrder),
]
