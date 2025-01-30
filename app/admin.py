from django.contrib import admin

from .models import About, Education, SchoolEducation,Skill,Project,CertificateCategory,Certificate

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(SchoolEducation)
admin.site.register(Project)
admin.site.register(CertificateCategory)
admin.site.register(Certificate)