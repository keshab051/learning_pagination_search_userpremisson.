from django.contrib import admin
from .models import Movies
# Register your models here.

admin.site.site_header ="E-commerce Site"


admin.site.register(Movies)