from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request,'index.html')


def login(request):
    if request.method=="POST":
        try:
            uid=request.POST.get("userid")
            ps=request.POST.get("pswd")
            if uid=='ethan' and ps=='chelsea':
                page="Recruiter.html"
            else:
                page="Failure.html"
        except:
            page="Failure.html"
    return render(request,page)

def newjob(request):
    return render(request,"NewJobEntry.html")

def addjob(request):
    if request.method=="POST":
        try:
            jobtitle=request.POST.get("jobtitle")
            recruiterid=int(request.POST.get("recruiterid"))
            qualifications=request.POST.get("qualifications").split(',')
            locations=request.POST.get("locations").split(',')
            skills=request.POST.get("skills").split(',')
            responsibilities=request.POST.get("responsibilities").split(',')
            annualpackage=float(request.POST.get("annualpackage"))
            experience=request.POST.get("experience")
            
            dic={}
            dic['jobtitle']=jobtitle
            dic['recruiterid']=recruiterid
            dic['qualifications']=qualifications
            dic['locations']=locations
            dic['skills']=skills
            dic['responsibilities']=responsibilities
            dic['annualpackage']=annualpackage
            dic['experience']=experience
            print(dic)

            requests.post('http://localhost:8080/jobs/add',json=dic)
            page="index.html"
        except Exception as err:
            print(err)
            page="Failure.html"
    return render(request,page)

        