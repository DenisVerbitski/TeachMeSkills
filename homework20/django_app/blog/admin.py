from django.contrib import admin

from blog.models import User, Post, Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','second_name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
