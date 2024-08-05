from django.contrib import admin
from . models import ImageModel, Category, AuthModel

# Register your models here.
admin.site.register(ImageModel)
admin.site.register(Category)
admin.site.register(AuthModel)
