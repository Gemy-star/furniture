from django.urls import path
from store import views

urlpatterns = [
    path('add/products', views.add_product, name='add-product'),
    path('products', views.search_products, name='search-product'),
    path('carts', views.checkout, name='carts'),
    path('products/all/reports', views.ProductAllReport.as_view(), name='report-products'),
    path('customers/all/reports', views.CustomerAllReport.as_view(), name='report-customers'),
    path('update/sessions', views.update_Session, name='update-session'),

]