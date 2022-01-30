from django.contrib import admin
from .models import Patient
from .models import Visit


# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Patient, PatientAdmin)


class VisitAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'problem', 'entry_date')

    def first_name(self, instance):
        return instance.patient.first_name

    def last_name(self, instance):
        return instance.patient.last_name


admin.site.register(Visit, VisitAdmin)
