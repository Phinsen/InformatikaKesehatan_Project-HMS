from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admit_patient_bed/', views.admit_patient_bed, name='admit_patient'),
    path('admit_patient_base/', views.admit_patient_base, name='admit_patient'),
]
