from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Season, Section, Department, Doctor, Patient, Registration   #, Period, Year

admin.site.register(Season)
admin.site.register(Section)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Registration)