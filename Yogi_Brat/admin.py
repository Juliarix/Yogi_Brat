from django.contrib import admin
from .models import Contact
from .models import Blog

admin.site.register(Blog)
admin.site.register(Contact)