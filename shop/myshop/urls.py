from django.urls import path
from . import views


app_name = 'myshop'


urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<int:category_id>/', views.product_list, name='product-list-by-category'),
    path('product/<int:product_id>', views.product_detail, name='product-detail')
]
