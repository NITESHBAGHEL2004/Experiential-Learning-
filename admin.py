from django.contrib import admin
from .models import academic_year,school, program, branch,faculty, semester, section, subject, pbl,PBLActivity


admin.site.register(academic_year)
admin.site.register(school)
admin.site.register(program)
admin.site.register(faculty)
admin.site.register(branch)
admin.site.register(semester)
admin.site.register(section)
admin.site.register(subject)
admin.site.register(pbl)
admin.site.register(PBLActivity)




