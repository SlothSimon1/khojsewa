"""
Models for Khoj Sewa application.
Stores Service providers and Service Requests.
"""
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import re


class CustomUser(models.Model):
    """
    Custom user model supporting both regular users and experts.
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Hashed password
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    years_experience = models.IntegerField(null=True, blank=True)  # Only for experts
    expertise = models.CharField(max_length=100, null=True, blank=True)  # E.g., Tutor, Electrician, Plumber
    location = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def set_password(self, raw_password):
        """Hash and set the password."""
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Check if the provided password matches the stored hash."""
        return check_password(raw_password, self.password)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.role})"


class Service(models.Model):
    """
    Represents a service provider in the system.
    """
    SERVICE_TYPES = [
        ('Tutor', 'Tutor'),
        ('Electrician', 'Electrician'),
        ('Plumber', 'Plumber'),
    ]
    
    LOCATIONS = [
        ('Kathmandu', 'Kathmandu'),
        ('Lalitpur', 'Lalitpur'),
        ('Bhaktapur', 'Bhaktapur'),
        ('Pokhara', 'Pokhara'),
        ('Biratnagar', 'Biratnagar'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    location = models.CharField(max_length=100, choices=LOCATIONS)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.type}"


class ServiceRequest(models.Model):
    """
    Represents a service request from a user.
    """
    REQUEST_STATUS = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    SERVICE_TYPES = [
        ('Tutor', 'Tutor'),
        ('Electrician', 'Electrician'),
        ('Plumber', 'Plumber'),
    ]
    
    LOCATIONS = [
        ('Kathmandu', 'Kathmandu'),
        ('Lalitpur', 'Lalitpur'),
        ('Bhaktapur', 'Bhaktapur'),
        ('Pokhara', 'Pokhara'),
        ('Biratnagar', 'Biratnagar'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests', null=True, blank=True)
    accepted_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_requests')
    type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    location = models.CharField(max_length=100, choices=LOCATIONS)
    problem = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=REQUEST_STATUS, 
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        user_name = self.user.name if self.user else 'Unknown User'
        return f"{user_name} - {self.type} ({self.status})"


class Rating(models.Model):
    """
    User ratings for experts (0-5 scale).
    """
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings_given')
    expert = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings_received')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    request = models.ForeignKey(ServiceRequest, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'expert', 'request')
        ordering = ['-created_at']
    
    def __str__(self):
        user_name = self.user.name if self.user else 'Unknown'
        expert_name = self.expert.name if self.expert else 'Unknown'
        return f"{user_name} rated {expert_name} - {self.rating}/5"


def validate_nepali_phone(phone):
    """
    Validate Nepali phone number format.
    Must start with 97 or 98 and be 10 digits total.
    """
    pattern = r'^(97|98)\d{8}$'
    return bool(re.match(pattern, phone))
