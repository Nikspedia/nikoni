from django.db import models
from django.contrib.auth.models import User


KELAS_CHOICES = [
    ('1', 'Kelas 1'),
    ('2', 'Kelas 2'),
    ('3', 'Kelas 3'),
    ('4', 'Kelas 4'),
    ('5', 'Kelas 5'),
    ('6', 'Kelas 6'),
]
HARI_CHOICES = [
    ('Senin', 'Senin'),
    ('Selasa', 'Selasa'),
    ('Rabu', 'Rabu'),
    ('Kamis', 'Kamis'),
    ('Jumat', 'Jumat'),
    ('Sabtu', 'Sabtu'),
]

MAPEL_CHOICES = [
    ('Bahasa Indonesia', 'Bahasa Indonesia'),
    ('Matematika', 'Matematika'),
    ('Ilmu Pengetahuan Alam', 'Ilmu Pengetahuan Alam'),
    ('Ilmu Pengetahuan Sosial', 'Ilmu Pengetahuan Sosial'),
    ('Pendidikan Pancasila dan Kewarganegaraan', 'PPKn'),
    ('Pendidikan Agama', 'Pendidikan Agama'),
    ('Seni Budaya dan Prakarya', 'SBdP'),
    ('Pendidikan Jasmani, Olahraga, dan Kesehatan', 'PJOK'),
    ('Bahasa Inggris', 'Bahasa Inggris'),
    ('Muatan Lokal', 'Muatan Lokal'),
]


class Guru(models.Model):
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=50, unique=True)
    mapel = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Siswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nis = models.CharField(max_length=50, unique=True)
    kelas = models.CharField(max_length=20, choices=KELAS_CHOICES)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class JadwalSiswa(models.Model):
    hari = models.CharField(max_length=20, choices=HARI_CHOICES)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    mapel = models.CharField(max_length=100, choices=MAPEL_CHOICES)
    siswa = models.ForeignKey(Siswa, on_delete=models.SET_NULL, null=True)
    kelas = models.CharField(max_length=20, choices=KELAS_CHOICES)

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
class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('guru', 'Guru'),
        ('siswa', 'Siswa'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    kelas = models.CharField(max_length=2, blank=True, null=True)  # kalau kamu butuh kelas siswa

    def __str__(self):
        return f"{self.user.username} - {self.role}"

