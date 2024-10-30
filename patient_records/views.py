# patient_records/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Patient, Assessment, AirwayAssessment, Investigations, Medications, AnaestheticPlan
from .forms import AirwayAssessmentForm, InvestigationsForm, MedicationsForm, AnaestheticPlanForm

def home(request):
    return render(request, 'patient_records/home.html')

def search_patient(request):
    results = []
    query = request.GET.get('query')  # Get the search query from the form
    if query:
        # Search for patients by ID, passport number, or full name (assuming these fields exist)
        results = Patient.objects.filter(
            Q(id_number__icontains=query) |  # Assuming the field for ID is `id_number`
            Q(passport_number__icontains=query) |  # Assuming the field for passport is `passport_number`
            Q(name__icontains=query)  # Assuming the field for full name is `name`
        )
    return render(request, 'patient_records/search_patient.html', {'results': results})


def add_full_patient_info(request):
    if request.method == "POST":
        # Patient details
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        medical_history = request.POST.get("medical_history")
        surgical_history = request.POST.get("surgical_history")
        social_history = request.POST.get("social_history")
        presenting_illness = request.POST.get("presenting_illness")

        # Create patient
        patient = Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            medical_history=medical_history,
            surgical_history=surgical_history,
            social_history=social_history,
            presenting_illness=presenting_illness
        )

        # Collect and create related data (e.g., assessments, meication)

        # Assessment details
        asa_classification = request.POST.get("asa_classification")
        allergies = request.POST.get("allergies")
        notes = request.POST.get("notes")
        
        # Create assessment linked to the patient
        Assessment.objects.create(
            patient=patient,
            asa_classification=asa_classification,
            allergies=allergies,
            notes=notes
        )

        # Airway assessment details
        mallampati_score = request.POST.get("mallampati_score")
        neck_mobility = request.POST.get("neck_mobility")
        dental_conditions = request.POST.get("dental_conditions")
        other_notes = request.POST.get("other_notes")

        # Create airway assessment linked to the patient
        AirwayAssessment.objects.create(
            patient=patient,
            mallampati_score=mallampati_score,
            neck_mobility=neck_mobility,
            dental_conditions=dental_conditions,
            other_notes=other_notes
        )

        # Investigations details
        test_name = request.POST.get("test_name")
        result = request.POST.get("result")
        test_date = request.POST.get("test_date")

        Investigations.objects.create(
            patient=patient,
            test_name=test_name,
            result=result,
            date=test_date
        )

        # Medications details
        medication_name = request.POST.get("medication_name")
        dosage = request.POST.get("dosage")
        frequency = request.POST.get("frequency")

        Medications.objects.create(
            patient=patient,
            name=medication_name,
            dosage=dosage,
            frequency=frequency
        )

        # Anaesthetic Plan details
        anaesthetic_technique = request.POST.get("anaesthetic_technique")
        anticipated_difficulties = request.POST.get("anticipated_difficulties")
        pre_op_instructions = request.POST.get("pre_op_instructions")
        post_op = request.POST.get("post_op")

        AnaestheticPlan.objects.create(
            patient=patient,
            anaesthetic_technique=anaesthetic_technique,
            anticipated_difficulties=anticipated_difficulties,
            pre_op_instructions=pre_op_instructions,
            post_op=post_op
        )

        return redirect('view_patients')  # Redirect to patient list after submission
    
    return render(request, 'patient_records/add_full_patient_info.html')

def view_patients(request):
    patients = Patient.objects.all()  # Retrieve all patients
    return render(request, 'patient_records/view_patients.html', {'patients': patients})

# Define add_assessment view function
def add_assessment(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        asa_classification = request.POST.get("asa_classification")
        allergies = request.POST.get("allergies")
        notes = request.POST.get("notes")
        
        Assessment.objects.create(
            patient=patient,
            asa_classification=asa_classification,
            allergies=allergies,
            notes=notes
        )
        return redirect('view_patient_assessments', patient_id=patient.id)
    
    return render(request, 'patient_records/add_assessment.html', {'patient': patient})

# Add view_patient_assessments function
def view_patient_assessments(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    # Assuming each model is linked to the Patient model with a ForeignKey
    assessments = Assessment.objects.filter(patient=patient)  # General assessments
    airway_assessments = AirwayAssessment.objects.filter(patient=patient)  # Airway assessments
    medications = Medications.objects.filter(patient=patient)  # Medications
    investigations = Investigations.objects.filter(patient=patient)  # Investigations
    anaesthetic_plans = AnaestheticPlan.objects.filter(patient=patient)  # Anaesthetic plans
    
    # Pass all related assessments to the template
    context = {
        'patient': patient,
        'assessments': assessments,
        'airway_assessments': airway_assessments,
        'medications': medications,
        'investigations': investigations,
        'anaesthetic_plans': anaesthetic_plans,
    }
    
    return render(request, 'patient_records/view_assessments.html', context)

# In views.py
# patient_records/views.py
from django.shortcuts import render, get_object_or_404
from .models import Patient, AirwayAssessment  # Make sure these models are imported
from .forms import AirwayAssessmentForm

def airway_assessment(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = AirwayAssessmentForm(request.POST)
        if form.is_valid():
            airway_assessment = form.save(commit=False)
            airway_assessment.patient = patient
            airway_assessment.save()
            return redirect('airway_assessment', patient_id=patient_id)
    else:
        form = AirwayAssessmentForm()
    return render(request, 'patient_records/airway_assessment_form.html', {'form': form, 'patient': patient})

def investigations(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == "POST":
        form = InvestigationsForm(request.POST)
        if form.is_valid():
            investigation = form.save(commit=False)
            investigation.patient = patient
            investigation.save()
            return redirect('investigations', patient_id=patient.id)
    else:
        form = InvestigationsForm()
    
    return render(request, 'patient_records/investigations.html', {'form': form, 'patient': patient})

def medications(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == "POST":
        form = MedicationsForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.patient = patient
            medication.save()
            return redirect('medications', patient_id=patient.id)
    else:
        form = MedicationsForm()
    
    return render(request, 'patient_records/medications.html', {'form': form, 'patient': patient})

def anaesthetic_plan(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == "POST":
        form = AnaestheticPlanForm(request.POST)
        if form.is_valid():
            anaesthetic_plan = form.save(commit=False)
            anaesthetic_plan.patient = patient
            anaesthetic_plan.save()
            return redirect('anaesthetic_plan', patient_id=patient.id)
    else:
        form = AnaestheticPlanForm()
    
    return render(request, 'patient_records/anaesthetic_plan.html', {'form': form, 'patient': patient})

