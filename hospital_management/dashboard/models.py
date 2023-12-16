from django.db import models

# Define a model for Patient's Basic Data
class Patient_Base(models.Model):
    ADMISSION_CHOICES = [
        ('admitted', 'Admitted'),
        ('not_admitted', 'Not Admitted'),
        # Add other choices as needed for Diagnosis, Beware, Admission Form, etc.
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    DEPARTMENT_CHOICES = [
        ('dept1', 'Department 1'),
        ('dept2', 'Department 2'),
        # Add other department choices
    ]

    STATION_CHOICES = [
        ('station1', 'Station 1'),
        ('station2', 'Station 2'),
        # Add other station choices
    ]

    INSURANCE_CHOICES = [
        ('insurance1', 'Insurance 1'),
        ('insurance2', 'Insurance 2'),
        # Add other insurance choices
    ]

    admission_number = models.CharField(max_length=50, primary_key=True)  # Admission Number
    last_name = models.CharField(max_length=100)  # Last Name
    first_name = models.CharField(max_length=100)  # First Name
    date_of_birth = models.DateTimeField()  # Date of Birth

    # Gestational Week
    gestational_week = models.CharField(max_length=50)

    size_cm = models.FloatField()  # Size
    weight_kg = models.FloatField()  # Weight

    # Automatically calculated fields
    bmi = models.FloatField()  # BMI (Calculate based on weight and size)
    bsa = models.FloatField()  # BSA (Calculate based on size and weight)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # Gender

    # Admission in Department and Hospital
    admission_in_department = models.DateTimeField()  # Admission in Department
    admission_in_hospital = models.DateTimeField()  # Admission in Hospital

    diagnosis = models.CharField(max_length=100, choices=ADMISSION_CHOICES)  # Diagnosis
    beware = models.CharField(max_length=100, choices=ADMISSION_CHOICES)  # Beware
    admission_form = models.CharField(max_length=100, choices=ADMISSION_CHOICES)  # Admission Form
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)  # Department
    station = models.CharField(max_length=100, choices=STATION_CHOICES)  # Station
    health_insurance = models.CharField(max_length=100, choices=INSURANCE_CHOICES)  # Health Insurance

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.admission_number}"  # Display patient's name and admission number

class Patient_General(models.Model):
    admission_number = models.ForeignKey(Patient_Base, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    patient_number = models.CharField(max_length=20, blank=True, null=True)

class Patient_ReferencePerson(models.Model):
    admission_number = models.ForeignKey(Patient_Base, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    relationship_with_patient = models.CharField(max_length=100, blank=True, null=True)

class BedOccupancy(models.Model):
    bed_number = models.CharField(max_length=20)
    occupied = models.BooleanField(default=False)
    occupied_since = models.DateTimeField(blank=True, null=True)
    admission_number = models.ForeignKey(Patient_Base, blank=True, null=True, on_delete=models.SET_NULL)

    def delete(self, *args, **kwargs):
        if self.bed_number in ['101', '102', '103', '104', '105', '106']:
            # Prevent deletion of default beds
            return
        super().delete(*args, **kwargs)