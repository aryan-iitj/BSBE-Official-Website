from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from Bio import Entrez
import socket
from django.contrib.auth.decorators import user_passes_test
from . import models
from . models import Research
from . models import NewsAndEvents
from . models import *
from . models import Projects
from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        ta_resource = TAResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = ta_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            ta_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, '/import.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def checkIP(request):
    accpetable = ["127", "172", "10."]
    ip = str(get_client_ip(request))
    print(ip)
    pref = ip[0:3]
    if pref in accpetable:
        return True
    return False

def index(request):
    resrch = Research.objects.all().order_by("-pk")
    # print(resrch)
    newsletter= NewsAndEvents.objects.all().order_by("-pk")
    # newsletter.reverse()
    print(newsletter)
    context = {'Research': resrch, 'NewsAndEvents':newsletter, 'display_intranet':checkIP(request)}
    return render(request,'home/index.html', context)

def academic(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/academic.html', context)


def technicalstaff(request):
    technicalstaff = Staff.objects.filter(StaffType='TechnicalStaff')
    context = {'StaffResults': technicalstaff, 'display_intranet': checkIP(request)}
    return render(request, 'home/technicalstaff.html', context)

def administrativestaff(request):
    administrativestaff = Staff.objects.filter(StaffType='Administrative Staff')
    context = {'StaffResults': administrativestaff, 'display_intranet': checkIP(request)}
    return render(request, 'home/technicalstaff.html', context)

def faculty_advisors(request):
    resultsdisplay= Faculty_Advisors.objects.all()
    sortedresultdisplay=resultsdisplay.order_by('name1')
    context = {'Faculty_Advisors':sortedresultdisplay, 'display_intranet': checkIP(request)}
    return render(request,'home/faculty_advisors.html',context)

def Phd_students(request):
    currentstudents=Current_PhdStudents.objects.all()
    graduatedstudents=Graduated_PhdStudents.objects.all()
    context={'currentstudents':currentstudents,'graduatedstudents':graduatedstudents, 'display_intranet': checkIP(request)}
    return render(request,'home/Phd_students.html',context)

def research(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/Research.html', context)

def researchAreas(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/ResearchAreas.html', context)

def CellandMolecularPhysiology(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/CellandMolecularPhysiology.html', context)

def EnvironmentalBiotechnology(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/EnvironmentalBiotechnology.html', context)

def BiomaterialsandTissueEngineering(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/BiomaterialsandTissueEngineering.html', context)

def ChemicalBiologyandDrugDesign(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/ChemicalBiologyandDrugDesign.html', context)

def MolecularMicrobiologyandMicrobialGenomics(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/MolecularMicrobiologyandMicrobialGenomics.html', context)

def Biophysics(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/Biophysics.html', context)

def ComputationalBiologyandBioinformatics(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/ComputationalBiologyandBioinformatics.html', context)

def MolecularMotorsandCellMotility(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/MolecularMotorsandCellMotility.html', context)

def NeuroscienceandNeuroengineering(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/NeuroscienceandNeuroengineering.html', context)

def projects(request):
    results= Projects.objects.all()
    context = {'projects':results, 'display_intranet': checkIP(request)}
    return render(request,'home/projects.html',context)

def SponsandColab(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/sponsandcolab.html', context)

def researchlabs(request):
    context = {'display_intranet': checkIP(request)}
    return render(request, 'home/researchlabs.html', context)

def webinars(request):
    # print(UpcomingWebinar.objects.filter().extra(select={"day_mod": "strftime('%d', Date)"}, order_by=['-day_mod']))
    Webinars = UpcomingWebinar.objects.filter().extra(select={"day_mod": "strftime('%d', Date)", "time_mod": "strftime('%H:%M', Time)"}, order_by=['-day_mod', '-time_mod'])
    # Webinars = UpcomingWebinar.objects.all()
    # print(Webinars)

    context = {'Webinars': Webinars, 'display_intranet': checkIP(request)}
    return render(request,'home/webinars.html', context)

def upcomingstudentppt(request):
    PPTS = UpcomingStudentPPT.objects.filter().extra(select={"day_mod": "strftime('%d', Date)", "time_mod": "strftime('%H:%M', Time)"}, order_by=['-day_mod', '-time_mod'])
    context = {'PPTS': PPTS, 'display_intranet': checkIP(request)}
    return render(request,'home/students_presentation.html', context)

#def students_presentation(request):
    #return render(request,'home/students_presentation.html')

def placements(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/placements.html', context)

def acm_student_chapter_iitj(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/acm_student_chapter_iitj.html', context)

def alumni(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/alumni.html', context)

def club_activity(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/club_activity.html', context)

def joinus(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/joinus.html', context)

def contacts(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/contacts.html', context)

def pubmed(request):

    #print(socket.gethostbyname(socket.gethostname()))
    if request.method == 'POST':
        query = request.POST.get('query')
        # print(query)
        if query == "":
            return redirect('pubmed')
        Entrez.email = "architshrikar25@gmail.com"
        handle = Entrez.esearch(db='pubmed',
                                sort='relevance',
                                retmax='20',
                                retmode='xml',
                                term=query)
        results = Entrez.read(handle)
        # print(results)
        ids = results['IdList']
        handle1 = Entrez.efetch(db='pubmed',
                                retmode='xml',
                                id=ids)
        res = Entrez.read(handle1)
        # print(res)
        # print(res['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle'])

        info = []

        for i, paper in enumerate(res['PubmedArticle']):
            # print("{}) {}".format(i + 1, paper['MedlineCitation']['Article']['ArticleTitle']))
            mydict = {}
            mydict['pmid'] = ids[i]
            mydict['title'] = paper['MedlineCitation']['Article']['ArticleTitle']
            mydict['link'] = "https://pubmed.ncbi.nlm.nih.gov/" + str(ids[i]) + "/"
            info.append(mydict)
        # print(info)
        context = {'articles': info, 'display_intranet': checkIP(request)}
        return render(request, 'home/srch.html', context)
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/srch.html', context)

def allresearch(request):
    researchhighlights = Research.objects.all().order_by("-pk")
    context = {'Research': researchhighlights, 'display_intranet': checkIP(request)}
    return render(request, 'home/allresearch.html', context)

def allnews(request):
    news = NewsAndEvents.objects.all().order_by("-pk")
    context = {'News': news, 'display_intranet': checkIP(request)}
    return render(request, 'home/allnews.html', context)

def Publications(request):
    resultsdisplay = Faculty_Advisors.objects.all()
    sortedresultdisplay = resultsdisplay.order_by('name1')
    AllFaculties = []
    for faculty in sortedresultdisplay:
        if str(faculty.FacultyType) == "RegularFaculty":
            AllFaculties.append(faculty)
    context = {"Faculties": AllFaculties, 'display_intranet': checkIP(request)}
    if request.method == "POST":
        query = request.POST.get('query')
        AllPub = PublicationList.objects.all()
        res = []
        for publication in AllPub:
            if query in str(publication.FullName):
                res.append(publication)
        context["Results"] = res
        # print(query)
        return render(request, 'home/IntraPublications.html', context)
    if (checkIP(request)):
        return render(request, 'home/IntraPublications.html', context)
    return render(request, 'home/NoIntranet.html', context)

def Awards(request):
    resultsdisplay = Faculty_Advisors.objects.all()
    sortedresultdisplay = resultsdisplay.order_by('name1')
    AllFaculties = []
    for faculty in sortedresultdisplay:
        if str(faculty.FacultyType) == "RegularFaculty":
            AllFaculties.append(faculty)
    context = {"Faculties": AllFaculties, 'display_intranet': checkIP(request)}
    if request.method == "POST":
        query = request.POST.get('query')
        AllAwards = AwardsList.objects.all()
        res = []
        for award in AllAwards:
            if query in str(award.FullName):
                res.append(award)
        context["Results"] = res
        # print(query)
        return render(request, 'home/Awards.html', context)
    if(checkIP(request)):
        return render(request, 'home/Awards.html', context)
    return render(request, 'home/NoIntranet.html', context)

def project_list(request):
    resultsdisplay = Faculty_Advisors.objects.all()
    sortedresultdisplay = resultsdisplay.order_by('name1')
    AllFaculties = []
    for faculty in sortedresultdisplay:
        if str(faculty.FacultyType) == "RegularFaculty":
            AllFaculties.append(faculty)
    context = {"Faculties": AllFaculties, 'display_intranet': checkIP(request)}
    if request.method == "POST":
        query = request.POST.get('query')
        AllProjects = ProjectsList.objects.all()
        res = []
        for project in AllProjects:
            if query in str(project.NameFaculty):
                res.append(project)
        context["Results"] = res
        # print(query)
        return render(request, 'home/FacultyProjects.html', context)
    if(checkIP(request)):
        return render(request, 'home/FacultyProjects.html', context)
    return render(request, 'home/NoIntranet.html', context)


def projectstudent_list(request):
    resultsdisplay = Faculty_Advisors.objects.all()
    sortedresultdisplay = resultsdisplay.order_by('name1')
    AllFaculties = []
    for faculty in sortedresultdisplay:
        if str(faculty.FacultyType) == "RegularFaculty":
            AllFaculties.append(faculty)
    context = {"Faculties": AllFaculties, 'display_intranet': checkIP(request)}
    if request.method == "POST":
        query = request.POST.get('query')
        AllStudents = ProjectsStudents.objects.all()
        res = []
        for projectstudent in AllStudents:
            if query in str(projectstudent.NameFaculty):
                res.append(projectstudent)
        context["Results"] = res
        # print(query)
        return render(request, 'home/FacultyProjectStudents.html', context)
    if(checkIP(request)):
        return render(request, 'home/FacultyProjectStudents.html', context)
    return render(request, 'home/NoIntranet.html', context)











def Students(request):
    context = {'display_intranet': checkIP(request)}
    if(checkIP(request)):
        return render(request, 'home/Students.html', context)
    return render(request, 'home/NoIntranet.html', context)

def Equipment(request):
    context = {'display_intranet': checkIP(request)}
    if(checkIP(request)):
        return render(request, 'home/equipment.html', context)
    return render(request, 'home/NoIntranet.html', context)

def TeachingAssistant(request):
    TAdetail= TA.objects.all().order_by("-pk")
    context = {'TA':TAdetail, 'display_intranet': checkIP(request)}
    if(checkIP(request)):
        return render(request, 'home/intranetTA.html', context)
    return render(request, 'home/NoIntranet.html', context)    
    
def AparatusDetails(request):
    Equipmentdetail= Apparatus.objects.all().order_by("-pk")
    context = {'Apparatus':Equipmentdetail, 'display_intranet': checkIP(request)}
    if(checkIP(request)):
        return render(request, 'home/equipment.html', context)
    return render(request, 'home/NoIntranet.html', context)    
    
def Btechug(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/bsbeugprogram.html', context)

def Mtechpg(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/Mtechinbsbe.html', context)

def PhDpg(request):
    context = {'display_intranet': checkIP(request)}
    return render(request,'home/Phdbsbe.html', context)
