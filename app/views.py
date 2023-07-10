from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]
job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description"
]

# Create your views here.

class TempClass:
    x = 5

def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name":"Django", "age":24, "first_list":list, "temp_object":temp, "is_authenticated": is_authenticated}
    return render(request, 'app/hello.html', context)

def job_list(request):
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url= reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    jobs = JobPost.objects.all()
    context = {'jobs':jobs}
    return render(request, 'app/index.html', context)
    

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        #context = {'job_title':job_title[id], 'job_description':job_description[id]}
        job = JobPost.objects.get(id=id)
        context = {'job':job}
        return render(request, 'app/job_detail.html', context)
    except:
        return HttpResponseNotFound("Not Found")