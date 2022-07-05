from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_case_aboutus_url(self):
        url=reverse('Home:aboutus')
        self.assertEquals(resolve(url).func,aboutus)  

    def test_case_blog_url(self):
        url=reverse('Home:blog')
        self.assertEquals(resolve(url).func,blog)

  