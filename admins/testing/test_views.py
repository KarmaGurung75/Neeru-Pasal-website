from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_admin_dashboard_get(self):
        client=Client()
        response=client.get(reverse('admin_dashboard'))
        self.assertTemplateUsed(response,'admins/homepage.html')

    def test_show_user_get(self):
        client=Client()
        response=client.get(reverse('show_users'))
        self.assertTemplateUsed(response,'admins/users.html')

    def test_show_admin_get(self):
        client=Client()
        response=client.get(reverse('show_admins'))
        self.assertTemplateUsed(response,'admins/admins.html')

    def test_register_user_get(self):
        client=Client()
        response=client.get(reverse('register_user'))
        self.assertTemplateUsed(response,'admins/adduser.html')



