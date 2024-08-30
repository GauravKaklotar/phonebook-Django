from django.contrib import admin
from .models import User, Contact, Spam

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email')
    search_fields = ('username', 'phone_number', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'user')
    search_fields = ('name', 'phone_number', 'user__username')

@admin.register(Spam)
class SpamAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    search_fields = ('phone_number',)