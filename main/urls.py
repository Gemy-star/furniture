from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('about', views.about_page, name='about_page'),
    path('reports', views.reports, name='reports')

]
