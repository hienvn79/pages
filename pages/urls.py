from django.urls import path
from .views import (HomeViewPage,AboutViewPage) # a class that inherit templateview to display a template

urlpatterns=[
    path("",view=HomeViewPage.as_view(),name="home"), #HomeViewPage.as_view()=> return a view
    path("about/",view=AboutViewPage.as_view(),name="about"),
]
print(f"urls:{urlpatterns}")
#path(route,view,name)