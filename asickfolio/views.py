from django.shortcuts import redirect,render
from app.models import About,Education,SchoolEducation,Skill,Project,CertificateCategory


def BASE(request):
    about_info = About.objects.first()
    education_info = Education.objects.all()
    skills = Skill.objects.all()
    school_education_info = SchoolEducation.objects.all()  # Assuming a single About entry
    projects = Project.objects.all()
    context = {
        "about":about_info,
        'education_info': education_info,
        'school_education_info': school_education_info,
        'skills':skills,
        "projects":projects
    }
    return render(request,'Main/home.html',context)

def CERTIFICATE(request):
    certificate_categories = CertificateCategory.objects.all()

    return render(request,'Certificate/certificate.html',{'certificate_categories': certificate_categories})