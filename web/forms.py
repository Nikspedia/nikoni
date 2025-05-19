from django import forms
from .models import Galeri, Siswa, JadwalSiswa, Berita, Guru

class GaleriForm(forms.ModelForm):
    class Meta:
        model = Galeri
        fields = '__all__'

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'

class JadwalSiswaForm(forms.ModelForm):
    class Meta:
        model = JadwalSiswa
        fields = '__all__'

class BeritaForm(forms.ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'

class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        fields = '__all__'

