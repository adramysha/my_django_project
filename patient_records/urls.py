from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view URL
    path('add/', views.add_full_patient_info, name='add_full_patient_info'),  # Add patient URL
    path('view/', views.view_patients, name='view_patients'),  # View full patient info

    # URL for specific assessments and details
    path('patients/<int:patient_id>/add_assessment/', views.add_assessment, name='add_assessment'),  # Add assessment
    path('patients/<int:patient_id>/assessments/', views.view_patient_assessments, name='view_patient_assessments'),  # View assessments

    # Additional URLs for adding detailed patient information sections
    path('patients/<int:patient_id>/airway_assessment/', views.airway_assessment, name='airway_assessment'),  # Add Airway Assessment
    path('patients/<int:patient_id>/investigations/', views.investigations, name='investigations'),  # Add Investigations
    path('patients/<int:patient_id>/medications/', views.medications, name='medications'),  # Add Medications
    path('patients/<int:patient_id>/anaesthetic_plan/', views.anaesthetic_plan, name='anaesthetic_plan'),  # Add Anaesthetic Plan

    # URLs for viewing each detailed section
    path('patients/<int:patient_id>/airway_assessment/', views.airway_assessment, name='airway_assessment'),  # View Airway Assessment
    path('patients/<int:patient_id>/investigations/', views.investigations, name='investigations'),  # View Investigations
    path('patients/<int:patient_id>/medications/', views.medications, name='medications'),  # View Medications
    path('patients/<int:patient_id>/anaesthetic_plan/', views.anaesthetic_plan, name='anaesthetic_plan'),  # View Anaesthetic Plan

    # Other URLs
    path('search/', views.search_patient, name='search_patient'),
]