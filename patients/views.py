from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from patients.models import Patient,Visit


def index(request):
    return render(request, 'index.html')


def patients(request):
    patients = Patient.objects.order_by('create_date_time')
    context = {'patients': patients}
    return render(request, 'patients.html', context)


def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    visits = Visit.objects.filter(patient=patient_id)
    context = {'patient': patient, 'visits': visits}
    return render(request, 'patient.html', context)
