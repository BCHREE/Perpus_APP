from django.contrib import admin
from django.urls import path
from peminjam import views

urlpatterns = [
    # Jalur Dashboard Utama
    path('', views.halaman_dashboard, name='url_dashboard'),
    
    # Jalur Buku (CRUD Master Buku)
    path('buku/', views.daftar_buku, name='url_buku'),
    path('buku/tambah/', views.halaman_tambah_buku, name='url_tambah_buku'),
    path('buku/edit/', views.halaman_edit_buku, name='url_edit_buku'),  # Mengarah ke halaman_edit_buku
    path('buku/hapus/', views.halaman_hapus_buku, name='url_hapus_buku'),  # Mengarah ke halaman_hapus_buku
    
    # Jalur Peminjaman (Transaksi)
    path('peminjaman/', views.daftar_peminjaman, name='url_peminjaman'),
    path('peminjaman/tambah/', views.halaman_pinjam_buku, name='url_tambah_pinjam'),
    
    # Jalur User (CRUD Anggota)
    path('user/', views.halaman_daftar, name='url_daftar'),
    path('user/tambah/', views.halaman_tambah_user, name='url_tambah_user'),
    path('user/detail/', views.halaman_detail_user, name='url_detail'),  # Mengarah ke halaman_detail_user
    path('user/edit/', views.halaman_edit_user, name='url_edit'),  # Mengarah ke halaman_edit_user
    path('user/hapus/', views.halaman_hapus_user, name='url_hapus'),  # Mengarah ke halaman_hapus_user
    
    path('admin/', admin.site.urls),
]