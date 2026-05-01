from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name}'
    
class Job(models.Model):
    Job_Type = (
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('remote','Remote'),
    )
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    job_type = models.CharField(max_length=20,choices=Job_Type)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    cover_letter = models.TextField(blank=True)

    class Meta:
        unique_together = ('user','job')

    def __str__(self):
        return f'{self.user.username} applied to {self.job.title}'


