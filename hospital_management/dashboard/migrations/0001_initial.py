# Generated by Django 4.2.7 on 2023-12-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Base',
            fields=[
                ('admission_number', models.CharField(primary_key=True, max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('gestational_week', models.CharField(max_length=50)),
                ('size_cm', models.FloatField()),
                ('weight_kg', models.FloatField()),
                ('bmi', models.FloatField()),
                ('bsa', models.FloatField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('admission_in_department', models.DateTimeField()),
                ('admission_in_hospital', models.DateTimeField()),
                ('diagnosis', models.CharField(choices=[('admitted', 'Admitted'), ('not_admitted', 'Not Admitted')], max_length=100)),
                ('beware', models.CharField(choices=[('admitted', 'Admitted'), ('not_admitted', 'Not Admitted')], max_length=100)),
                ('admission_form', models.CharField(choices=[('admitted', 'Admitted'), ('not_admitted', 'Not Admitted')], max_length=100)),
                ('department', models.CharField(choices=[('dept1', 'Department 1'), ('dept2', 'Department 2')], max_length=100)),
                ('station', models.CharField(choices=[('station1', 'Station 1'), ('station2', 'Station 2')], max_length=100)),
                ('health_insurance', models.CharField(choices=[('insurance1', 'Insurance 1'), ('insurance2', 'Insurance 2')], max_length=100)),
            ],
        ),
    ]
