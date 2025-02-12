from django.contrib import admin
from .models import Category, Product, Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ['name', 'message']

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact, ContactAdmin)