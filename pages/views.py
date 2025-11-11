from django.shortcuts import render
from django.views.generic import TemplateView #built-in function to create a template

# Create your views here: a class-based view
#Home View page
class HomeViewPage(TemplateView): #inherit template class
    """
      template_name (must): TemplateResponseMixin requires either a definition of 'template_name'
    """
    template_name="home.html" # a field of class
#About View Page
class AboutViewPage(TemplateView):
    template_name="about.html"
