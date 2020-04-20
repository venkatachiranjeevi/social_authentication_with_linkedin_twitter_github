
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser


# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password', 'name', 'last_login')}),
#         ('Permissions', {'fields': (
#             'is_active',
#             'is_staff',
#             'is_superuser',
#             'groups',
#             'user_permissions',
#         )}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': ('email', 'password1', 'password2')
#             }
#         ),
#     )
#
#     list_display = ('email', 'name')
#     list_filter = ('email', 'name')
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(CustomUser)