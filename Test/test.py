from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from homepages.views import about, delete_gallery_modelform, contact
from homepages.models import ProductCategory, ProductList

class TestUrls(SimpleTestCase):
    def test_about(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_delete_gallery_modelform_url(self):
        url = reverse('delete_gallery_modelform', args=[1])
        self.assertEquals(resolve(url).func, delete_gallery_modelform)

    def test_contactus_url(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.show_gallery_url = reverse('show_gallery')
        self.contact_url = reverse('contact')
    def test_gallery(self):
        response = self.client.get(self.show_gallery_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepages/gallery.html')
    def test_contact(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepages/contact.html')

class TestModels(TestCase):
    def setUp(self):
        self.product_list = ProductList.objects.create(
            product_name='Local Apple',
            product_price="260"
        )
        self.product_category = ProductCategory.objects.create(
            category_name='Local Product',
            category_info="Pure mustang loacl apple",
        )
    def test_product_list_model(self):
        self.assertEquals(self.product_list.food_name, 'Local Apple')
    def test_food_category_model(self):
        self.assertEquals(self.product_category.category_name, 'Local product')

