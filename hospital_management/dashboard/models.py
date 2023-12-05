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

    admission_number = models.CharField(max_length=50)  # Admission Number
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
