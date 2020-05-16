from django.contrib import admin
from .models import officialwebsites
from .models import location
from .models import drive

# Register your models here.
admin.site.register(officialwebsites)
admin.site.register(location)
admin.site.register(drive)
