from django.test import SimpleTestCase
from homepages.forms import  *


class TestForms(SimpleTestCase):
    def test_order_form(self):
        form=OrderForm(data={
            'quantity':'1',
            'contact_no':'98765268',
            'contact_address':'swayambhunath, kathmandu',
            'payment_method':'esewa',
        })
        self.assertTrue(form.is_valid())

    def test_order_form(self):
        form=OrderForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

    def test_contact_form(self):
        cform=FeedbackForm(data={
                'name':'karma',
                'email ':'sonam@gmail.com',
                'subject':'Better product',
                'message':'The product are more better',
            })
        self.assertFalse(cform.is_valid())

    def test_order_form(self):
        cform=FeedbackForm(data={})

        self.assertFalse(cform.is_valid())
        self.assertEquals(len(cform.errors),5)


    


