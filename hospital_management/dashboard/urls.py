from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admit_patient/', views.admit_patient, name='admit_patient'),
]
