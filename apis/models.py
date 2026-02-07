from django.db import models

# Create your models here.

class SchoolPartnershipInquiry(models.Model):
    school_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    school_location = models.CharField(max_length=255)
    grades_available = models.CharField(max_length=100)
    approx_student_count = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name
    

class EnrollmentInquiry(models.Model):
    student_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    grade = models.CharField(max_length=50)
    preferred_track = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name