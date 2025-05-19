from django.shortcuts import render, get_object_or_404, redirect
from .models import Galeri, Siswa, JadwalSiswa, Berita, Guru
from .forms import GaleriForm, SiswaForm, JadwalSiswaForm, BeritaForm, GuruForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # kalau sudah login, langsung ke home

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username atau password salah.')

    return render(request, 'login.html', {'title': 'Login'})

def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'web/home.html', {'title': 'Dashboard'})

# GALERI
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Galeri
from .forms import GaleriForm

def galeri_list(request):
    galeri = Galeri.objects.all().order_by('-tanggal_upload')
    return render(request, 'web/galeri_list.html', {'galeri': galeri})

def galeri_create(request):
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto berhasil ditambahkan.')
            return redirect('galeri_list')
    else:
        form = GaleriForm()
    return render(request, 'web/admin/galeri_form.html', {'form': form, 'title': 'Tambah Foto'})

def galeri_update(request, pk):
    galeri = get_object_or_404(Galeri, pk=pk)
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES, instance=galeri)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto berhasil diperbarui.')
            return redirect('galeri_list')
    else:
        form = GaleriForm(instance=galeri)
    return render(request, 'web/admin/galeri_form.html', {'form': form, 'title': 'Edit Foto'})

def galeri_delete(request, pk):
    galeri = get_object_or_404(Galeri, pk=pk)
    galeri.delete()
    messages.success(request, 'Foto berhasil dihapus.')
    return redirect('galeri_list')


# SISWA
def siswa_list(request):
    siswa = Siswa.objects.all()
    return render(request, 'siswa_list.html', {'siswa': siswa})

def siswa_create(request):
    if request.method == 'POST':
        form = SiswaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('siswa_list')
    else:
        form = SiswaForm()
    return render(request, 'form.html', {'form': form, 'title': 'Tambah Siswa'})

def siswa_update(request, pk):
    siswa = get_object_or_404(Siswa, pk=pk)
    if request.method == 'POST':
        form = SiswaForm(request.POST, request.FILES, instance=siswa)
        if form.is_valid():
            form.save()
            return redirect('siswa_list')
    else:
        form = SiswaForm(instance=siswa)
    return render(request, 'form.html', {'form': form, 'title': 'Edit Siswa'})

def siswa_delete(request, pk):
    siswa = get_object_or_404(Siswa, pk=pk)
    if request.method == 'POST':
        siswa.delete()
        return redirect('siswa_list')
    return render(request, 'confirm_delete.html', {'object': siswa, 'title': 'Hapus Siswa'})

def jadwal_form(request, pk=None):
    if pk:
        jadwal = get_object_or_404(JadwalSiswa, pk=pk)
        title = 'Edit Jadwal'
    else:
        jadwal = None
        title = 'Tambah Jadwal'

    if request.method == 'POST':
        form = JadwalSiswaForm(request.POST, instance=jadwal)
        if form.is_valid():
            form.save()
            return redirect('jadwal_list')
    else:
        form = JadwalSiswaForm(instance=jadwal)

    return render(request, 'web/admin/jadwal_form.html', {'form': form, 'title': title, 'jadwal': jadwal})

def jadwal_delete(request, pk):
    jadwal = get_object_or_404(JadwalSiswa, pk=pk)
    if request.method == 'POST':
        jadwal.delete()
        return redirect('jadwal_list')
    return render(request, 'web/admin/confirm_delete.html', {'object': jadwal, 'title': 'Hapus Jadwal'})

def jadwal_list(request):
    jadwal = JadwalSiswa.objects.all()
    return render(request, 'web/admin/jadwal_list.html', {'jadwal': jadwal})



def berita_list(request):
    berita = Berita.objects.all()
    return render(request, 'web/admin/berita_list.html', {'berita': berita})

def berita_form(request, pk=None):
    if pk:
        berita = get_object_or_404(Berita, pk=pk)
        title = 'Edit Berita'
    else:
        berita = None
        title = 'Tambah Berita'

    if request.method == 'POST':
        form = BeritaForm(request.POST, instance=berita)
        if form.is_valid():
            form.save()
            return redirect('berita_list')
    else:
        form = BeritaForm(instance=berita)

    return render(request, 'web/admin/berita_form.html', {'form': form, 'title': title, 'berita': berita})

def berita_delete(request, pk):
    berita = get_object_or_404(Berita, pk=pk)
    if request.method == 'POST':
        berita.delete()
        messages.success(request, 'Berita berhasil dihapus.')
        return redirect('berita_list')
    # Kalau mau, bisa redirect langsung tanpa render confirm delete
    return redirect('berita_list')


# GURU
def guru_list(request):
    guru = Guru.objects.all()
    return render(request, 'guru_list.html', {'guru': guru})

def guru_create(request):
    if request.method == 'POST':
        form = GuruForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guru_list')
    else:
        form = GuruForm()
    return render(request, 'form.html', {'form': form, 'title': 'Tambah Guru'})

def guru_update(request, pk):
    guru = get_object_or_404(Guru, pk=pk)
    if request.method == 'POST':
        form = GuruForm(request.POST, request.FILES, instance=guru)
        if form.is_valid():
            form.save()
            return redirect('guru_list')
    else:
        form = GuruForm(instance=guru)
    return render(request, 'form.html', {'form': form, 'title': 'Edit Guru'})

def guru_delete(request, pk):
    guru = get_object_or_404(Guru, pk=pk)
    if request.method == 'POST':
        guru.delete()
        return redirect('guru_list')
    return render(request, 'confirm_delete.html', {'object': guru, 'title': 'Hapus Guru'})


