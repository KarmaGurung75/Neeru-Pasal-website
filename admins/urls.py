from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name="admin_dashboard"),
    path('users', views.show_users, name="show_users"),
    path('admins', views.show_admins, name="show_admins"),
    path('promote/<int:user_id>', views.promote_user, name="promote_user"),
    path('demote/<int:user_id>', views.demote_admin, name="demote_admin"),
    path('register', views.register_user, name="register_user"),
]