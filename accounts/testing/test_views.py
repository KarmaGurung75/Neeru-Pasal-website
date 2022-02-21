from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_homepage(self):
        client=Client()
        response=client.get(reverse('homepage'))
        self.assertTemplateUsed(response,'accounts/homepage.html')

    def test_login(self):
        client=Client()
        response=client.get(reverse('login_user'))
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_register(self):
        client=Client()
        response=client.get(reverse('register_user'))
        self.assertTemplateUsed(response,'accounts/register.html')
