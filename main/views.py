from django.shortcuts import render, redirect
from .models import Job
from django.contrib import messages
def index(request):
    return render(request,'index.html') 
def job_inquiry(request):
    return render(request, 'job.html')
def contact_us(request):
    return render(request,'contact.html')
def gallery_page(request):
    return render(request,'slider.html')
def addjob(request):
    errors = Job.objects.job_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/jobinquiry')
    else:
        all_jobs = Job.objects.all()
        new_job = Job.objects.create(
            customer_name = request.POST['customer_name'],
            job_desc = request.POST['job_desc'],
            location = request.POST['location'],
            email_address = request.POST['email'],
            phone_number = request.POST['phone_number']
        )
    return  redirect('/submitted')
def submitjob(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs' : all_jobs
        }
    return render(request,'submit_page.html',context)
def price_page(request):
    return render(request,'pricing.html')
def product_page(request):
    return render(request,'products.html')
def jobs_display(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs' : all_jobs
        }
    return render(request,'jobs.html',context)
def delete_job(request):
    job_to_delete = Job.objects.get(id=request.POST['job_id'])
    job_to_delete.delete()
    return redirect('/jobs')