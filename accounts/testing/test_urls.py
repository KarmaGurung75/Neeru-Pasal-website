from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import *


class TestUrls(SimpleTestCase):
    def test_home_page_urls_is_resolved(self):
        url=reverse('homepage')
        view=resolve(url).func
        self.assertEquals(view,homepage)

    def test_login_user_urls_is_resolved(self):
        url=reverse('login')
        view=resolve(url).func
        self.assertEquals(view,login_user)

    def test_register_user_urls_is_resolved(self):
        url=reverse('logout')
        view=resolve(url).func
        self.assertEquals(view,logout_user)

    def test_profile_urls_is_resolved(self):
        url=reverse('my_profile')
        view=resolve(url).func
        self.assertEquals(view,profile)

    def test_update_profile_urls_is_resolved(self):
        url=reverse('edit_profile')
        view=resolve(url).func
        self.assertEquals(view,edit_profile)

    def test_password_change_password_user_urls_is_resolved(self):
        url=reverse('homepage')
        view=resolve(url).func
        self.assertEquals(view,homepage)

    def test_change_password_user_urls_is_resolved(self):
        url=reverse('password_change')
        view=resolve(url).func
        self.assertEquals(view,change_password)

    # def test_password_change_admin_urls_is_resolved(self):
    #     url=reverse('password_change_admin')
    #     view=resolve(url).func
    #     self.assertEquals(view,change_password)



