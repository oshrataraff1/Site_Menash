from django.contrib import admin
from firstapp.models import GeneralInfo, Service, Testimonial

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    
    list_display = [
        'company_name',
        'location',
        'email',
        'phone',
        'open_hours',
        
    ]
    
    # show to disable add permission
    def has_add_permission(self, request, obj=None):
        return False
    
    # show to disable update permission
    def has_change_permission(self, request, obj=None):
        return False
    
    # show to disable delete permission
    def has_delete_permission(self, request, obj=None):
        return False
    
    # show to disable update permission for a specific field
    readonly_fields = [
        'company_name'
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
        list_display = [
        'title',
        'description',
        ]
        
        search_fields = [
            "title",
            "description",
        ]
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    
    list_display = [
        'username',
        'user_job_title',
        'display_rating_count',
        ]
    
    
    def display_rating_count(self, obj):
        return '*' * obj.rating_count
    
    display_rating_count.short_description = 'Rating'