# Use include() to add paths from the catalog application 
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from .import views


app_name='oursite'
urlpatterns = [    
    path('',views.index,name='index'),
    path('contact-us', views.contact ,name='contact'),
    path('register',views.register, name='register'),
    path('about-us',views.about_us, name='about_us'),
    path('services',views.services, name='services'),
    path('products',views.products,name='products'),
]
