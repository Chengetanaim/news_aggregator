from django.contrib import admin
from .models import News
from .models import Job


admin.site.register(News)
admin.site.register(Job)