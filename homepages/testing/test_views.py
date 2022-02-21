from django.test import TestCase,Client
from django.urls import reverse


# Here we are testing the views ..
#  we test if views are rendering correct templates or not
# we get urls via reverse function and pass value to .assertTemplateUsed with expeted template with actual template

class Test_views(TestCase):
    def test_about(self):
        client=Client()
        response=client.get(reverse('about'))
        self.assertTemplateUsed(response,'homepages/about.html')

    def test_show_gallery(self):
        client=Client()
        response=client.get(reverse('show_gallery'))
        self.assertTemplateUsed(response,'homepages/gallery.html')

    def test_contact(self):
        client=Client()
        response=client.get(reverse('contact'))
        self.assertTemplateUsed(response,'homepages/contact.html')
