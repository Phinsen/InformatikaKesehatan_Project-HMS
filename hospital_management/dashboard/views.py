from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import AdmissionForm, BedForm
from .models import Patient_Base, BedOccupancy

def dashboard_view(request):
    bed_occupancy_data = BedOccupancy.objects.all()
    patient_data = Patient_Base.objects.all()
    return render(request, 'dashboard/dashboard.html', {'bed_occupancy_data': bed_occupancy_data, 'patient_data': patient_data})

def admit_patient_bed(request):
    if request.method == 'POST':    
        form = BedForm(request.POST)
        if form.is_valid():
            bed_number = form.cleaned_data['bed_number']
            admission_number = form.cleaned_data['admission_number']

            try:
                bed_occupy = BedOccupancy.objects.get(bed_number=bed_number)
                bed_occupy.occupied = True
                bed_occupy.occupied_since = timezone.now()  
                bed_occupy.admission_number_id = admission_number  # Assign the admission_number foreign key ID
                
                bed_occupy.save()  # Save the changes
                
                return render(request, 'dashboard/success_page.html')
            
            except BedOccupancy.DoesNotExist:
                return HttpResponseServerError('Bed not found.')  # Error if the bed is not found
            
            except Exception as e:
                return HttpResponseServerError(f'Error: {str(e)}')  # General error message for any other exception
            
        else:
            print(form.errors)
            return render(request, 'dashboard/failed_page.html')
    else:
        form = BedForm()
        
    return render(request, 'dashboard/dashboard.html', {'form': form})

def admit_patient_base(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        # bed_occupancy.cleaned_data['admission_number'] = patient_base_data.cleaned_data['admission_number']
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/success_page.html')
        else:
            return render(request, 'dashboard/failed_page.html')
    else:
        form = AdmissionForm()
    return render(request, 'dashboard/dashboard.html', {'form': form})