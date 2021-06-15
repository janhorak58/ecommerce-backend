from django.urls import path
from base.views import product_views as views


urlpatterns = [
    


    #path('', views.getRoutes, name="routes"),
    path('', views.getProducts, name="products"),
    path('update/<str:pk>/', views.updateProduct, name="update-product"),
    path('delete/<str:pk>', views.deleteProduct, name="delete-product"),
    path('create/', views.createProduct, name="create-product"),
    path('upload/', views.uploadImage, name="upload-image"),
    path('<str:pk>/', views.getProduct, name="product"),
    

]
