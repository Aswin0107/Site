from django.contrib import admin

# Register your models here.
from .models import Change,Actor
admin.site.register(Change)
admin.site.register(Actor)