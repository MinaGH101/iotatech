from django.contrib import admin
from .models import *


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):      
    list_display = ('id', 'title', 'category')
    search_fields = ('title',)
    list_filter = ('created',)


@admin.register(Project)
class PostAdmin(admin.ModelAdmin):      
    list_display = ('id', 'title', 'employee')
    search_fields = ('title',)
    list_filter = ('created',)
    
    
@admin.register(Category)
class PostAdmin(admin.ModelAdmin):      
    list_display = ('id', 'name')

# @admin.register(Promo)
# class PostAdmin(admin.ModelAdmin):      
#     list_display = ('id', 'code', 'discount')


# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Project)
# admin.site.register(CartItem)
# admin.site.register(Vote)
# admin.site.register(Shipping)


