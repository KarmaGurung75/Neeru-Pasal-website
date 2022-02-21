from django.test import SimpleTestCase
from accounts.forms import  ProfileForm


class TestForms(SimpleTestCase):
    def test_login_form(self):
        form=ProfileForm(data={
           'user':'',
           'username':'Karma',
           'email':'Karma1661@gmail.com',
           'firstname':'Karma',
           'lastname':'Gurung',
           'phone':'982756536',
           'profile_piture':'image.jpg'
            
        })
        self.assertTrue(form.is_valid())