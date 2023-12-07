from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Count
from django.utils.html import format_html,urlencode
from django.urls import reverse


@admin.register(User)
class UserAdmin(BaseUserAdmin):
        list_display=['full_name','post_count']
        search_fields=['first_name__icontains']
        
        add_fieldsets = (
    (
        None,
        {
            "classes": ("wide",),
            "fields": ("first_name","last_name","email","username", "password1", "password2"),
        },
    ),
)  
        
        def full_name(self,user):
                return f"{user.first_name} {user.last_name}"
                        
        
        @admin.display(ordering='post_count')
        def post_count(self,user):
                url=reverse('admin:primary_post_changelist')+'?'+urlencode({
                        "user_id":str(user.id)
                })
                return format_html("<a href='{}' target='_blank'>{} </a>",url,user.post_count)
        
        
        def get_queryset(self, request):
                return super().get_queryset(request).annotate(post_count=Count('post'))
                
