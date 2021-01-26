from django.contrib import admin
from .models import *

class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)

class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'city_state', 'start_date', 'currently_employed', )
    list_filter = ('currently_employed',)
    search_fields = ['company',]

class JobDutyAdmin(admin.ModelAdmin):
    list_display = ('company', 'duty',)
    list_filter = ('company',)
    search_fields = ['company',]

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'gpa', 'start_date', 'currently_enrolled', )
    list_filter = ('currently_enrolled',)
    search_fields = ['school',]

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('certification',)
    search_fields = ['certification',]

class PersonalSkillAdmin(admin.ModelAdmin):
    list_display = ('skill',)
    search_fields = ['skill',]

class ComputerSkillAdmin(admin.ModelAdmin):
    list_display = ('skill',)
    search_fields = ['skill',]

class InterestsAdmin(admin.ModelAdmin):
    list_display = ('interest',)
    search_fields = ['interest',]

admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobDuty, JobDutyAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(PersonalSkill, PersonalSkillAdmin)
admin.site.register(ComputerSkill, ComputerSkillAdmin)
admin.site.register(Interests, InterestsAdmin)
