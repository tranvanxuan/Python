from django.urls import path
from .import views

urlpatterns = [
    path('', views.ShowProduct, name='index'),
    path('productdetail/<int:id>/', views.ProductDetail, name='detail'),
    path('add/', views.add, name='add' ),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]