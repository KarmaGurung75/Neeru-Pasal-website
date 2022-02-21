from django.test import SimpleTestCase
from django.urls import reverse,resolve
from admins.views import *


class TestUrls(SimpleTestCase):
    def test_admin_dashboard_urls_is_resolved(self):
        url=reverse('admin_dashboard')
        view=resolve(url).func
        self.assertEquals(view,admin_dashboard)

    def test_view_users_urls_is_resolved(self):
        url=reverse('show_users')
        view=resolve(url).func
        self.assertEquals(view,show_users)

    def test_view_admins_urls_is_resolved(self):
        url=reverse('show_admins')
        view=resolve(url).func
        self.assertEquals(view,show_admins)

    def test_promote_user_urls_is_resolved(self):
        url=reverse('promote_user', args=['1'])
        view=resolve(url).func
        self.assertEquals(view,promote_user)

    def test_demote_admins_urls_is_resolved(self):
        url=reverse('demote_admin', args=['2'])
        view=resolve(url).func
        self.assertEquals(view,demote_admin)

    def test_register_user_urls_is_resolved(self):
        url=reverse('register_user')
        view=resolve(url).func
        self.assertEquals(view,register_user)