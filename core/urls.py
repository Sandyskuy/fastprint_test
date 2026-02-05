from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:id>/', views.edit_produk, name='edit_produk'),
    path('hapus/<int:id>/', views.hapus_produk, name='hapus_produk'),
]
