from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(GameItem)
admin.site.register(BookItem)
admin.site.register(MovieItem)
admin.site.register(Register)


