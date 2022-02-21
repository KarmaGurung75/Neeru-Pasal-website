from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.login_user, name="login"),
    path('register', views.register_user, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('my_profile', views.profile, name="my_profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('password_change', views.change_password, name="password_change"),
]