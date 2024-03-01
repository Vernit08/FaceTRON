from django.contrib import admin

# Register your models here.
from .models import Register
admin.site.register(Register)

from .models import Attendance
admin.site.register(Attendance)

