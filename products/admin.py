from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass
class ProductAdmin(admin.ModelAdmin):
    exclude = ['slug']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)

