from django.urls import path
from . import views
from .views import AddProductView, UpdateProductView, DeleteProductView


app_name = 'shop'

urlpatterns = [
    path('home', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('home/about/', views.about, name='about'),
    path('home/register/', views.register, name='register'),
    path('home/delivery/', views.delivery, name='delivery'),
    path('home/create/', AddProductView.as_view(), name='create'),
    path('home/update/<slug:pk>/', UpdateProductView.as_view(), name='update'),
    path('home/<slug:pk>/delete', DeleteProductView.as_view(), name='delete'),

]