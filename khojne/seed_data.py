"""
Script to populate Khoj Sewa database with sample services.
Run with: python manage.py shell < seed_data.py
"""

from main.models import Service

# Sample services data
services_data = [
    # Tutors
    {"name": "Ramesh Sharma", "type": "Tutor", "location": "Kathmandu", "phone": "+977-9841234567"},
    {"name": "Priya Poudel", "type": "Tutor", "location": "Lalitpur", "phone": "+977-9842345678"},
    {"name": "Arjun Adhikari", "type": "Tutor", "location": "Bhaktapur", "phone": "+977-9843456789"},
    {"name": "Deepa Joshi", "type": "Tutor", "location": "Pokhara", "phone": "+977-9844567890"},
    
    # Electricians
    {"name": "Sanjay Rai", "type": "Electrician", "location": "Kathmandu", "phone": "+977-9845678901"},
    {"name": "Ravi Kumar", "type": "Electrician", "location": "Lalitpur", "phone": "+977-9846789012"},
    {"name": "Bikram Singh", "type": "Electrician", "location": "Bhaktapur", "phone": "+977-9847890123"},
    {"name": "Naresh Tamang", "type": "Electrician", "location": "Biratnagar", "phone": "+977-9848901234"},
    
    # Plumbers
    {"name": "Mohan Khadka", "type": "Plumber", "location": "Kathmandu", "phone": "+977-9849012345"},
    {"name": "Dinesh Shrestha", "type": "Plumber", "location": "Lalitpur", "phone": "+977-9840123456"},
    {"name": "Anish Thapa", "type": "Plumber", "location": "Pokhara", "phone": "+977-9851234567"},
    {"name": "Suresh Magar", "type": "Plumber", "location": "Biratnagar", "phone": "+977-9852345678"},
]

# Clear existing services
Service.objects.all().delete()

# Create new services
for data in services_data:
    Service.objects.create(**data)

print(f"✓ Successfully created {len(services_data)} sample services!")
print("\nServices added to database:")
for service in Service.objects.all():
    print(f"  - {service.name} ({service.type}) - {service.location}")
