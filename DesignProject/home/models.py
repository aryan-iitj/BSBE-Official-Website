from pickle import TRUE
from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
# Create your models here.

class Research(models.Model):
    title = models.CharField(max_length=255, default="title")
    link = models.CharField(max_length=255, default="title")

class Projects(models.Model):
    Title=models.TextField()
    Investigators=models.TextField()
    FundingAgencies=models.TextField()
    CompletionYear=models.IntegerField()
    TechnologyTrack=models.TextField(blank=True)

class NewsAndEvents(models.Model):
    title = models.CharField(max_length=255, default="title")
    link = models.CharField(max_length=255, default="title")

class Faculty_Advisors(models.Model):
    name1=models.CharField(max_length=100)
    designation=models.CharField(max_length=700)
    email=models.EmailField(max_length = 254,blank=True)
    image=models.ImageField(upload_to='images/')
    #phoneNumberRegex = RegexValidator(regex=r"((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}")
    #phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16 , blank=True)
    phoneNumber = models.TextField(max_length = 25)
    phd=models.CharField(max_length=700,blank=True)
    domain = models.CharField(max_length=900,blank=True)
    faculty_type = (
        ('RegularFaculty', 'RegularFaculty'),
        ('YoungFacultyAssociates', 'YoungFacultyAssociates'),
        ('GuestFaculty', 'GuestFaculty'),
        ('AdjunctFaculty', 'AdjunctFaculty'),
        ('ScholarsinResidence', 'ScholarsinResidence'),
        ('Advisors', 'Advisors'),
        ('FormerFaculty', 'FormerFaculty'),
    )
    FacultyType = models.CharField(max_length=60, choices=faculty_type, blank=True)

class Staff(models.Model):
    name1=models.CharField(max_length=100)
    designation=models.CharField(max_length=700)
    email=models.EmailField(max_length = 254,blank=True)
    image=models.ImageField(upload_to='images/')
    staff_type = (
        ('TechnicalStaff', 'TechnicalStaff'),
        ('Administrative Staff', 'Administrative Staff'),
    )
    StaffType = models.CharField(max_length=60, choices=staff_type, blank=True)
    #phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    #phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16 , blank=True)
    Education = models.TextField(max_length = 700,default="")

class Current_PhdStudents(models.Model):
    Name=models.CharField(max_length=100)
    DegreeType_Recent=models.CharField(max_length=700)
    DomainOfStudy= models.CharField(max_length=900)
    CollegeName=models.CharField(max_length=900)
    CollegePassingYear=models.IntegerField()
    Supervisor = models.CharField(max_length=900)
    ResearchArea = models.CharField(max_length=900)
    image = models.ImageField(upload_to='images/')

class Graduated_PhdStudents(models.Model):
    Name=models.CharField(max_length=100)
    GraduationYear=models.IntegerField()
    Supervisor = models.CharField(max_length=900)
    ResearchArea = models.CharField(max_length=900)
    ThesisTitle = models.CharField(max_length=900)
    CurrentPosition = models.CharField(max_length=900)
    image = models.ImageField(upload_to='images/')

class UpcomingWebinar(models.Model):
    Date = models.DateField(default=datetime.datetime.now().date())
    Time = models.TimeField(default=datetime.datetime.now().time())
    Speaker = models.CharField(default="Name of Speaker", max_length=50)
    Title = models.CharField(default="Title of talk", max_length=200)
    Abstract = models.TextField(default="Abstract of Talk")
    image = models.ImageField(default='images/11.jpg', upload_to='images/')

class UpcomingStudentPPT(models.Model):
    Date = models.DateField(default=datetime.datetime.now().date())
    Time = models.TimeField(default=datetime.datetime.now().time())
    Presenter = models.CharField(default="Name of Speaker", max_length=50)
    Topic = models.CharField(default="Title of talk", max_length=200)
    image = models.ImageField(default='images/11.jpg', upload_to='images/')
    
class TA(models.Model):
    Name=models.CharField(max_length=100)
    Roll=models.CharField(max_length=100)
    Category=models.CharField(max_length=400)
    CourseWorkStatus=models.CharField(max_length=400)
    Supervisior=models.CharField(max_length=400)
    PreviousTAship=models.CharField(max_length=400)

class Apparatus(models.Model):
    Equipment=models.CharField(max_length=400)
    Installation_Location=models.CharField(max_length=100)
    PI_Project=models.CharField(max_length=400)
    PI=models.CharField(max_length=400)
    Last_maintainence_date=models.CharField(max_length=400)
    Details=models.CharField(max_length=400)

class PublicationList(models.Model):
    FullName = models.CharField(max_length=200, default="Full name")
    Authors = models.CharField(max_length=200)
    Title = models.CharField(max_length=400)
    Journal = models.CharField(max_length=100)
    Vol = models.CharField(max_length=100)
    Year = models.IntegerField(_('year'))
    DOI = models.CharField(max_length=100)

class AwardsList(models.Model):
    FullName = models.CharField(max_length=200, default="Full name")
    FacultyName = models.CharField(max_length=50)
    AwardName = models.CharField(max_length=200)
    AwardingBody = models.CharField(max_length=400)
    Year = models.IntegerField()
    Details = models.CharField(max_length=100, default='-')

class ProjectsList(models.Model):
    NameFaculty = models.CharField(max_length=50)#identifier
    Faculty=models.CharField(max_length=80)
    ProjectNo=models.IntegerField()
    ProjectTitle=models.CharField(max_length=100)
    FundingAgency=models.CharField(max_length=200)
    SanctionedAmount=models.CharField(max_length=50)
    Duration = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    FinancialYear = models.IntegerField()
    Details = models.CharField(max_length=100, default='-')


class ProjectsStudents(models.Model):
    NameFaculty = models.CharField(max_length=50)#identifier
    Name=models.CharField(max_length=80)
    RollNo=models.CharField(max_length=80)
    Category=models.CharField(max_length=100)
    SupervisiorI = models.CharField(max_length=100)
    SupervisiorII = models.CharField(max_length=100,blank=True)
    project_type = (
        ('BTP', 'BTP'),
        ('MTech', 'MTech'),
        ('MTech', 'MTech'),
        ('MTech-Phd', 'MTech-Phd'),
        ('Phd','Phd')
    )
    ProjectType = models.CharField(max_length=60, choices=project_type)
    SRCMemberI = models.CharField(max_length=100, blank=True)
    SRCMemberII = models.CharField(max_length=100, blank=True)
    SRCMemberIII = models.CharField(max_length=100, blank=True)
    ProjectTitle = models.CharField(max_length=100)
    ThesisSubmission=models.CharField(max_length=100)
    Defence=models.CharField(max_length=100)
    Remarks=models.CharField(max_length=100,blank=True)