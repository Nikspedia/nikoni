from django.db import models
from django.contrib.auth.models import User

class Guru(models.Model):
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=50, unique=True)
    mapel = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='guru/', blank=True, null=True)

    def __str__(self):
        return self.nama

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    nis = models.CharField(max_length=50, unique=True)
    kelas = models.CharField(max_length=20)
    alamat = models.TextField()
    foto = models.ImageField(upload_to='siswa/', blank=True, null=True)

    def __str__(self):
        return self.nama

class JadwalSiswa(models.Model):
    hari = models.CharField(max_length=20)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    mapel = models.CharField(max_length=100)
    guru = models.ForeignKey(Guru, on_delete=models.SET_NULL, null=True)
    kelas = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.kelas} - {self.mapel} ({self.hari})"

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita/')
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

class Galeri(models.Model):
    judul = models.CharField(max_length=200)
    gambar = models.ImageField(upload_to='galeri/')
    keterangan = models.TextField(blank=True, null=True)
    tanggal_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul




# models.py (contoh)
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('guru', 'Guru'),
        ('siswa', 'Siswa'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

