from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

admin.site.register(models.Endereco)
admin.site.register(models.Aluguel)

class ImagemInLine(admin.TabularInline):
    model = models.FotoDecoracao
    extra = 1

class DecoracaoAdmin(admin.ModelAdmin):
    inlines = [ImagemInLine]
admin.site.register(models.Decoracao, DecoracaoAdmin)

class TelefoneInline(admin.TabularInline):
    model = models.TelefoneSalao
    extra = 1

class SalaoAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline]
admin.site.register(models.Salao, SalaoAdmin)


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name','phone')}),
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
                    'phone',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )

admin.site.register(models.User, UserAdmin)
