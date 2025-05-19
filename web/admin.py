from django.contrib import admin
from .models import Guru, Siswa, JadwalSiswa, Berita, Galeri, Profile

@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nip', 'mapel')
    search_fields = ('nama', 'nip', 'mapel')

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nis', 'kelas')
    search_fields = ('nama', 'nis', 'kelas')
    list_filter = ('kelas',)

@admin.register(JadwalSiswa)
class JadwalSiswaAdmin(admin.ModelAdmin):
    list_display = ('hari', 'jam_mulai', 'jam_selesai', 'mapel', 'guru', 'kelas')
    list_filter = ('hari', 'kelas', 'mapel')
    search_fields = ('mapel', 'kelas', 'guru__nama')

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')
    search_fields = ('judul', 'isi')
    list_filter = ('tanggal',)

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_upload')
    search_fields = ('judul', 'keterangan')
    list_filter = ('tanggal_upload',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)
