from django.db import models

from django.db import models
import re 


class JobManager(models.Manager):
    def job_validator(self,postData):
        errors = {}
        if len(postData['customer_name']) < 2:
            errors['customer_name'] = "Name must be more than 2 characters!"
        if len(postData['job_desc']) < 5:
            errors['job_desc'] = "Description must be more than 5 characters!"
        if len(postData['location']) < 5:
            errors['location'] = "Location must be more than 5 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters!"
        return errors
            
class Job(models.Model):
    customer_name = models.CharField(max_length=255)
    job_desc = models.TextField()
    location = models.CharField(max_length=255)
    phone_number = models.CharField(default = 000, max_length = 20)
    email_address = models.CharField(default = "no email", max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()

