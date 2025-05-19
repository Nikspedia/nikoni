from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('galeri/', views.galeri_list, name='galeri_list'),
    path('galeri/create/', views.galeri_create, name='galeri_create'),
    path('galeri/edit/<int:pk>/', views.galeri_update, name='galeri_update'),
    path('galeri/delete/<int:pk>/', views.galeri_delete, name='galeri_delete'),
    path('siswa/', views.siswa_list, name='siswa_list'),    
    path('berita/', views.berita_list, name='berita_list'),
    path('berita/create/', views.berita_form, name='berita_create'),
    path('berita/update/<int:pk>/', views.berita_form, name='berita_update'),
    path('berita/delete/<int:pk>/', views.berita_delete, name='berita_delete'),
    path('guru/', views.guru_list, name='guru_list'),
    path('jadwal/', views.jadwal_list, name='jadwal_list'),
    path('jadwal/create/', views.jadwal_form, name='jadwal_create'),           # buat create
    path('jadwal/update/<int:pk>/', views.jadwal_form, name='jadwal_update'),  # buat update
    path('jadwal/delete/<int:pk>/', views.jadwal_delete, name='jadwal_delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
