from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    usertype=[
        ('job_recruiter','job_recruiter'),
        ('job_seeker','job_seeker'),
    ]
    display_name=models.CharField(max_length=100,null=True)
    usertype=models.CharField(choices=usertype,max_length=100,null=True)
    
    # Jobseeker
    skills=models.CharField(max_length=100,null=True)
    resume=models.FileField(upload_to='static/resume',null=True,default='None')
    education=models.CharField(max_length=100,null=True)
    qualifications=models.CharField(max_length=100,null=True)
    
    # Jobrecruiter
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=100,null=True)
    company_description=models.TextField(null=True)
    

class jobmodel(models.Model):
    category=[
        ('full_time','Full_Time'),
        ('part_time','Part_Time'),
    ]
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100,null=True)
    number_of_openings=models.CharField(max_length=100,null=True)
    category=models.CharField(choices=category,max_length=100,null=True)
    job_description=models.TextField(null=True)
    skills=models.CharField(max_length=100,null=True)
    
class applyjob(models.Model):
    applied_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    apply_to=models.ForeignKey(jobmodel,on_delete=models.CASCADE,null=True)
    skills=models.CharField(max_length=100,null=True)
    resume=models.FileField(upload_to='static/resumeforjob')
    status=models.CharField(max_length=100, default='pending')
    
class recruiterprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True, related_name='RecruiterProfile')
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=100,null=True)
    company_description=models.TextField(null=True)
    

class seekerprofile(models.Model):
    myuser=models.OneToOneField(customuser,on_delete=models.CASCADE,null=True, related_name='SeekerProfile')
    skills=models.CharField(max_length=100,null=True)
    resume=models.FileField(upload_to='static/resume')