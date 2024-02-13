from django.contrib import admin
from user.models import UserModel
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """import admin

    Args:
        admin (type): description
    """
admin.site.register(UserModel,UserAdmin)