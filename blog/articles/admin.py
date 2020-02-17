from django.contrib import admin

# Register your models here.
from .models import  Article,Mydynamic

admin.site.register(Article)
admin.site.register(Mydynamic)