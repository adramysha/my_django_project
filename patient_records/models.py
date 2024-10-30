from django.db import models

class Patient(models.Model):
    # Basic information
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    id_number = models.CharField(max_length=50, blank=True, null=True)
    hospital_id = models.CharField(max_length=50, blank=True, null=True)

    # Clinical Information
    diagnosis = models.CharField(max_length=255, blank=True)
    scheduled_operation = models.CharField(max_length=255, blank=True)
    date_of_operation = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    
# Patient profile
    height = ?
    weight = ?
    BMI = 
    Unit = 

    medical_history = models.TextField(blank=True)
    surgical_history = models.TextField(blank=True)
    social_history = models.TextField(blank=True)
    presenting_illness = models.TextField(blank=True)
    

class Assessment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='assessments')
    asa_classification = models.CharField(max_length=20)
    allergies = models.TextField(blank=True)
    height = 
    weight = 
    
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Assessment for {self.patient.name}"
    
class AirwayAssessment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="airway_assessments")
    mallampati_score = models.CharField(max_length=20)
    neck_mobility = models.CharField(max_length=50, blank=True)
    dental_conditions = models.TextField(blank=True)
    other_notes = models.TextField(blank=True)

    def __str__(self):
        return f"Airway Assessment for {self.patient.name}"
    
class Investigations(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="investigations")
    test_name = models.CharField(max_length=20)
    result = models.CharField(max_length=50, blank=True)
    date = models.TextField(blank=True)

    def __str__(self):
        return f"Investigations for ({self.test.name}) for {self.patient.name}"

class Medications(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medications")
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return f"Medication: {self.name} for {self.patient.name} - Dosage: {self.dosage}, Frequency:{self.frequency}"

class AnaestheticPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="anaesthetic_plan")
    anaesthetic_technique = models.CharField(max_length=20)
    anticipated_difficulties = models.CharField(max_length=50, blank=True)
    pre_op_instructions = models.TextField(blank=True)
    post_op = models.TextField(blank=True)

    def __str__(self):
        return f"Anaesthetic Plan for {self.patient.name}"
    