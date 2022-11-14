from django.contrib import admin
from .models import Game


admin.site.register(Game)
# Register your models here.
admin.site.site_header = "Conect 4 game"
admin.site.site_title = "connect 4 by Khaled Yasser"
admin.site.index_title = "Use the below tabs to control the application as an admin"