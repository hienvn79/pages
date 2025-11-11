from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class HomePageTest(TestCase): #inherit TestCase class
    """
     tests: url,available url by name, correct name of template, whether or not template contains
    """
    def test_url_exists_at_correct_location(self): #prefix: test_
        response=self.client.get("/") # return a response object
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response=self.client.get(reverse('home')) #reverse('home')=> a route that defined in urls.py ?
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response,"home.html")
    
    def test_template_contain(self):
        response=self.client.get(reverse('home'))
        self.assertContains(response,"<h1>Home page</h1>")

class AboutPageTest(TestCase):
    def test_url_exists_at_correct_location(self): 
        response=self.client.get("/about/") # return a response object
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response=self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        response=self.client.get(reverse('about'))
        self.assertTemplateUsed(response,"about.html")
    
    def test_template_contain(self):
        response=self.client.get(reverse('about'))
        self.assertContains(response,"<h1>About page</h1>")