from django.contrib import admin
from .models import posts


admin.site.register(posts)
# Register your models here.
admin.site.site_header = "News Feed App"
admin.site.site_title = "News Feed App by Khaled Yasser"
admin.site.index_title = "Use the below tabs to control the application as an admin"