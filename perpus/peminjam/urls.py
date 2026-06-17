from django.urls import path
from . import views

urlpatterns = [
    # Dashboard utama
    path('dashboard/', views.halaman_dashboard, name='url_dashboard'),
    
    # Kelola User
    path('', views.halaman_daftar, name='url_daftar'), 
    path('user/tambah/', views.halaman_tambah_user, name='url_tambah_user'),
    path('user/detail/', views.halaman_detail, name='url_detail'),
    path('user/edit/', views.halaman_edit, name='url_edit'),
    path('user/hapus/', views.halaman_hapus, name='url_hapus'),
    
    # Buku & Peminjaman
    path('buku/', views.daftar_buku, name='url_buku'),
    path('transaksi/', views.daftar_peminjaman, name='url_peminjaman'),
    path('peminjaman/kembalikan/', views.halaman_kembalikan_buku, name='url_kembalikan_buku'),
] # <-- Pastikan tanda kurung siku ini ada dan tidak terhapus! 