from django.urls import path
from users import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.register, name='signup'),

]
