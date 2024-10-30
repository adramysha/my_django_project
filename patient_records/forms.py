# patient_records/forms.py

from django import forms
from .models import AirwayAssessment, Investigations, Medications, AnaestheticPlan

class AirwayAssessmentForm(forms.ModelForm):
    class Meta:
        model = AirwayAssessment
        fields = ['mallampati_score', 'neck_mobility', 'dental_conditions', 'other_notes']

class InvestigationsForm(forms.ModelForm):
    class Meta:
        model = Investigations
        fields = ['test_name', 'result', 'date']

class MedicationsForm(forms.ModelForm):
    class Meta:
        model = Medications
        fields = ['name', 'dosage', 'frequency']

class AnaestheticPlanForm(forms.ModelForm):
    class Meta:
        model = AnaestheticPlan
        fields = ['anaesthetic_technique', 'anticipated_difficulties', 'pre_op_instructions', 'post_op']