from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests


def index(request):
    return render(request,'index.html')


@csrf_exempt
def findjobs(request):
    if request.method=="POST":
        try:
            skill=request.POST.get("skill")
            location=request.POST.get("location")
            #http://localhost:8013/jobs/search
            sk=[]
            sk.append(skill)
            loc=[]
            loc.append(location)
            dic={}
            dic['skills']=sk
            dic['locations']=loc
            resp=requests.post('http://localhost:8013/jobs/search',json=dic)
            
            dic['response']=resp.json()
            mess="success"
        except:
            mess='failed'
    return render(request,'jobresponse.html',dic)
    