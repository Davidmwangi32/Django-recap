from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
    search_fields = ('name', 'email')
    list_filter = ('age',)
    ordering = ('name',)
    
    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
        ('Additional Information', {
            'fields': ('age', 'bio')
        }),
    )
    
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True