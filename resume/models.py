from django.contrib import messages
from django.db import models

class GeneralInfo(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='My Name')
    email = models.EmailField(max_length=255, null=False, verbose_name='My Email')
    phone = models.CharField(max_length=255, null=False, verbose_name='My Phone Number')
    city_state = models.CharField(max_length=255, null=False, verbose_name='My Location')
    linkedin = models.CharField(max_length=255, null=False, verbose_name='My LinkedIn')
    github = models.CharField(max_length=255, null=False, verbose_name='My Git')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'General Information'
        verbose_name_plural = 'General Information'

class Job(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    company = models.CharField(max_length=255, null=False, verbose_name='Company Name')
    position = models.CharField(max_length=255, null=False, verbose_name='Position Title')
    city_state = models.CharField(max_length=255, null=False, verbose_name='Location')
    start_date = models.DateField(max_length=255, null=False, verbose_name='Start Date')
    end_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='End Date')
    currently_employed = models.BooleanField(choices=BOOL_CHOICES, default=False, null=False, verbose_name='Currently Employed Here')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-currently_employed',]

class JobDuty(models.Model):
    company = models.ForeignKey(Job, related_name='duty', on_delete=models.CASCADE, verbose_name='Company')
    duty = models.CharField(max_length=255, null=False, verbose_name='Duty')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    class Meta:
        verbose_name = 'Job Duties'
        verbose_name_plural = 'Job Duties'
        ordering = ['company',]

class Education(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    school = models.CharField(max_length=255, null=False, verbose_name='School Name')
    degree = models.CharField(max_length=255, null=False, verbose_name='Degree Title')
    gpa = models.CharField(max_length=255, null=False, verbose_name='GPA')
    city_state = models.CharField(max_length=255, null=False, verbose_name='Location')
    start_date = models.DateField(max_length=255, null=False, verbose_name='Start Date')
    end_date = models.DateField(max_length=255, null=True, blank=True, verbose_name='End Date')
    currently_enrolled = models.BooleanField(choices=BOOL_CHOICES, default=False, null=False, verbose_name='Currently Enrolled Here')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    def __str__(self):
        return self.school

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ['-currently_enrolled',]

class Certification(models.Model):
    certification = models.CharField(max_length=255, null=False, verbose_name='Certification')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    class Meta:
        verbose_name = 'Certifications'
        verbose_name_plural = 'Certifications'
        ordering = ['certification',]

class PersonalSkill(models.Model):
    skill = models.CharField(max_length=255, null=False, verbose_name='Skill')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    class Meta:
        verbose_name = 'Personal Skills'
        verbose_name_plural = 'Personal Skills'
        ordering = ['skill',]

class ComputerSkill(models.Model):
    skill = models.CharField(max_length=255, null=False, verbose_name='Skill')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    class Meta:
        verbose_name = 'Computer Skills'
        verbose_name_plural = 'Computer Skills'
        ordering = ['skill',]

class Interests(models.Model):
    interest = models.CharField(max_length=255, null=False, verbose_name='Interest')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')

    class Meta:
        verbose_name = 'Interests'
        verbose_name_plural = 'Interests'
        ordering = ['interest',]

