from django.contrib import admin

from .models import Link, SideBar

from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.

@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'create_time')
    fields = ('title', 'href', 'status', 'weight')
    
@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'create_time')
    fields = ('title', 'display_type', 'content')