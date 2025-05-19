from django.db.models.signals import post_migrate, post_save
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from .models import Profile

@receiver(post_migrate)
def create_roles_groups(sender, **kwargs):
    roles = ['admin', 'guru', 'siswa']
    for role_name in roles:
        Group.objects.get_or_create(name=role_name)

@receiver(post_save, sender=Profile)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        # Hapus user dari semua grup dulu supaya gak numpuk
        instance.user.groups.clear()
        # Tambah user ke grup sesuai role
        group = Group.objects.get(name=instance.role)
        instance.user.groups.add(group)

@receiver(post_save, sender=Profile)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        instance.user.groups.clear()
        try:
            group = Group.objects.get(name=instance.role)
            instance.user.groups.add(group)
        except ObjectDoesNotExist:
            pass  # Atau bisa log kesalahan kalau mau
