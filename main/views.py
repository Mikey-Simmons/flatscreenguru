from django.shortcuts import render, redirect
from .models import Job, User
from django.contrib import messages
import bcrypt
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
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash
    )
    messages.success(request,"User Successfully created!")
    request.session['user_id'] = new_user.id
    return redirect('/welcome')
def welcome(request):
    if 'user_id' in request.session:
        logged_in_user = User.objects.get(id=request.session['user_id'])
        all_jobs = Job.objects.all()
        context = {
        'logged_in_user': logged_in_user,
        'all_jobs' : all_jobs
        }
        return render(request,'jobs.html',context)
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/') 
    list_of_users = User.objects.filter(email=request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/welcome')

    return redirect('/')
def admin(request):
    return render(request,'admin.html')