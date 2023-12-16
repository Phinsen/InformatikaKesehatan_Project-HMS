from django.db import migrations
from dashboard.models import BedOccupancy

def create_default_beds(apps, schema_editor):
    BedOccupancy.objects.bulk_create([
        BedOccupancy(bed_number='106'),
        BedOccupancy(bed_number='105'),
        BedOccupancy(bed_number='104'),
        BedOccupancy(bed_number='103'),
        BedOccupancy(bed_number='102'),
        BedOccupancy(bed_number='101'),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0003_bedoccupancy'),  # Replace with the appropriate previous migration
    ]

    operations = [
        migrations.RunPython(create_default_beds),
    ]
