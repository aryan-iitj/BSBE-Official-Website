from django.contrib import admin
#from . models import NewsAndEvents, Research ,Faculty_Advisors,Staff,Current_PhdStudents,Graduated_PhdStudents,Projects,UpcomingWebinar,UpcomingStudentPPT,TA,Apparatus
from . models import *
from django.forms import TextInput, Textarea
from django.db import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class resize(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

class TAAdmin(ImportExportModelAdmin):
    pass

class ApparatusAdmin(ImportExportModelAdmin):
    pass
class PublicationListAdmin(ImportExportModelAdmin):
    pass
class AwardsListAdmin(ImportExportModelAdmin):
    pass
class ProjectsListAdmin(ImportExportModelAdmin):
    pass
class ProjectsStudentsAdmin(ImportExportModelAdmin):
    pass

class ProjectsAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Research)
admin.site.register(NewsAndEvents)
admin.site.register(Faculty_Advisors,resize)
admin.site.register(Staff,resize)
admin.site.register(Current_PhdStudents)
admin.site.register(Graduated_PhdStudents)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(UpcomingWebinar)
admin.site.register(UpcomingStudentPPT)

admin.site.register(TA,TAAdmin)
admin.site.register(Apparatus,ApparatusAdmin)
admin.site.register(PublicationList,PublicationListAdmin)
admin.site.register(AwardsList,AwardsListAdmin)
admin.site.register(ProjectsList,ProjectsListAdmin)
admin.site.register(ProjectsStudents,ProjectsStudentsAdmin)