from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

admin.site.register(models.Endereco)
admin.site.register(models.Aluguel)

# Configuração para adição de numero do saão

class TelefoneInline(admin.TabularInline):
    model = models.TelefoneSalao
    extra = 1

class SalaoAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline]
admin.site.register(models.Salao, SalaoAdmin)

## -- ##


# Configuração para adição de passage_id no admin

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'passage_id')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )

admin.site.register(models.User, UserAdmin)

## -- ##