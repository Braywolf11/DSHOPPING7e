from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(categories)
admin.site.register(country)
admin.site.register(clients)
admin.site.register(product)
admin.site.register(gender)
admin.site.register(shopping)

