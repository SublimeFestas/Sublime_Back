from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um endereço de email")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        grupo, _ = Group.objects.get_or_create(name='cliente')
        user.groups.add(grupo)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def telefones_display(self):
        return ", ".join([t.numero for t in self.telefones.all()])
    telefones_display.short_description = "Telefones"

class TelefoneUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='telefones', verbose_name='Usuário')
    numero = models.CharField(max_length=15, verbose_name='Número do telefone')

    def __str__(self):
        return f'{self.user.email} ({self.numero})'
