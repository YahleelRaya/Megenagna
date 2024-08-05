from django.db import models
from .db_connection import db

# Create your models here.

users_collection=db['Worker_Coll']
class Worker(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    EDUCATION_CHOICES = [
        ('LessThanHS', 'Less Than High School'),
        ('Highschool', 'Highschool'),
        ('Tradeschool', 'Trade School'),
        ('University', 'University'),
    ]

    JOB_TYPE_CHOICES = [
        ('Cooking', 'Cooking'),
        ('Cleaning', 'Cleaning'),
        ('Babysitting', 'Babysitting'),
        ('Other', 'Other'),
    ]

    SCHEDULE_CHOICES = [
        ('LiveIn', 'Live In'),
        ('Commute', 'Commute'),
    ]

    EXPERIENCE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    LANGUAGE_CHOICES = [
        ('Amharic', 'Amharic'),
        ('Oromigna', 'Oromigna'),
        ('Tigrigna', 'Tigrigna'),
        ('Somaligna', 'Somaligna'),
        ('Sidamigna', 'Sidamigna'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    education_history = models.CharField(max_length=15, choices=EDUCATION_CHOICES)
    government_id = models.FileField(upload_to='ids/')
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    other_job = models.CharField(max_length=50, blank=True, null=True)
    schedule = models.CharField(max_length=7, choices=SCHEDULE_CHOICES)
    experience = models.CharField(max_length=3, choices=EXPERIENCE_CHOICES)
    employer_name = models.CharField(max_length=100, blank=True, null=True)
    employer_phone = models.CharField(max_length=15, blank=True, null=True)
    employment_length = models.CharField(max_length=50, blank=True, null=True)
    languages = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    other_language = models.CharField(max_length=50, blank=True, null=True)
    reference_name = models.CharField(max_length=100)
    reference_phone = models.CharField(max_length=15)
    reference_email = models.EmailField(blank=True, null=True)
    reference_address = models.CharField(max_length=200)
    reference_id = models.FileField(upload_to='reference_ids/')
    agreement_signature = models.CharField(max_length=100) 