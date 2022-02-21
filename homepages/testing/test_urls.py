from django.test import SimpleTestCase
from django.urls import reverse,resolve
from homepages.views import *

class TestUrls(SimpleTestCase):
    def test_about_is_resolved(self):
      url=reverse('about')
      view=resolve(url).func
      self.assertEquals(view,about)

    def test_ShowList_is_resolved(self):
      url=reverse('show_list', args=[1])
      view=resolve(url).func
      self.assertEquals(view,show_list)

    def test_gallery_is_resolved(self):
      url=reverse('show_gallery')
      view=resolve(url).func
      self.assertEquals(view,show_gallery)

    def test_contact_is_resolved(self):
      url=reverse('contact')
      view=resolve(url).func
      self.assertEquals(view,contact)

    def test_ShowCart_is_resolved(self):
        url=reverse('show_cart_items')
        view=resolve(url).func
        self.assertEquals(view,show_cart_items)

    def test_wishlist_is_resolved(self):
      url=reverse('my_wishlist')
      view=resolve(url).func
      self.assertEquals(view,show_mywishlist)

    def test_my_order_is_resolved(self):
        url=reverse('my_order')
        view=resolve(url).func
        self.assertEquals(view,my_order)
