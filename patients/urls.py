from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('patients/', views.patients),
    path('patients/<int:patient_id>/', views.patient)
]