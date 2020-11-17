from django.shortcuts import render, redirect
from .models import Job

def index(request):
    return render(request,'index.html') 
def job_inquiry(request):
    return render(request, 'job.html')
def contact_us(request):
    return render(request,'contact.html')
def gallery_page(request):
    return render(request,'slider.html')
def addjob(request):
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
    return render(request,'submit_page.html')
def price_page(request):
    return render(request,'pricing.html')
def product_page(request):
    return render(request,'products.html')