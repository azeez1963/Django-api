from django.urls import path
from rest_framework.authtoken import views as auth_view
from . import views

urlpatterns=[
      # path('users', views.UserRegisterEndpoint.as_view(), name='create-user'),
      # path('login', auth_view.ObtainAuthToken.as_view(), name= 'login-user'),
      path('category', views.UpgradedCategoryEndpoint.as_view(), name='category'),
      path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name ='category_single'),
      path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name ='category-delete'),
      path('product', views.UpgradedProductEndpoint.as_view(), name='product-details'),
      path('product-list', views.ProductListEndpoint.as_view(), name='product-list'),
      path('product/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='product_id'),
      
]