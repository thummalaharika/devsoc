from random import random
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(destination)
admin.site.register(restaurants)
admin.site.register(menu)
admin.site.register(comment)
# admin.site.register(user)