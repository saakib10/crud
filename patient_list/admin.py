from django.contrib import admin

from .models import PatientDetails

@admin.register(PatientDetails)
class PatientDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','serial','name','doctor')
