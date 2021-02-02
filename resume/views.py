from django.shortcuts import render
from .models import GeneralInfo, Job, JobDuty, Certification, PersonalSkill, ComputerSkill, Interests, Education

def view_resume(request):
    gen_info = GeneralInfo.objects.all()
    jobs = Job.objects.all().order_by('-start_date')
    certifications = Certification.objects.values_list('certification', flat=True).extra(select={'certification': 'lower(certification)'}).order_by('certification')
    personal_skills = PersonalSkill.objects.values_list('skill', flat=True).extra(select={'skill': 'lower(skill)'}).order_by('skill')
    computer_skills = ComputerSkill.objects.values_list('skill', flat=True).extra(select={'skill': 'lower(skill)'}).order_by('skill')
    interests = Interests.objects.values_list('interest', flat=True).extra(select={'interest': 'lower(interest)'}).order_by('interest')
    #school = Education.objects.all().order_by('-start_date')
    schools = Education.objects.all()

    #if geninfo.exists() and jobs.exists() and duties.exists():
    if gen_info.exists() and jobs.exists() and personal_skills.exists() and computer_skills.exists() and \
            certifications.exists() and interests.exists() and schools.exists():
        context = {'gen_info': gen_info[0], 'jobs': jobs, 'certifications' : certifications, 'personal_skills' : personal_skills, \
                   'computer_skills' : computer_skills, 'interests' : interests, 'schools' : schools, }
        return render(request, 'resume/resume.html', context)
    else:
        return render(request, 'resume/resume.html', {'error' : ''})

def view_aboutme(request):
    gen_info = GeneralInfo.objects.all()

    #if geninfo.exists() and jobs.exists() and duties.exists():
    if gen_info.exists():
        context = {'gen_info': gen_info[0], }
        return render(request, 'resume/about_me.html', context)
    else:
        return render(request, 'resume/about_me.html', {'error' : ''})

