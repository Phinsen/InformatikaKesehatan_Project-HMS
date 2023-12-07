from django.shortcuts import render
from .forms import AdmissionForm

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def admit_patient(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the validated form data to the database
            # Redirect or perform actions after successful submission
    else:
        form = AdmissionForm()

    return render(request, 'dashboard/dashboard.html', {'form': form})
