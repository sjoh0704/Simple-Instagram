from django.contrib import admin
from django.db import models
from .models import Content, Image
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline] # content에서 Image를 편하게 볼 수 있게 하기 위함
    list_display = ('user', 'text',)


admin.site.register(Content, ContentAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)

