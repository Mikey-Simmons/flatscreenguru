from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('jobinquiry',views.job_inquiry),
    path('contact',views.contact_us),
    path('gallery',views.gallery_page),
    path('addjob',views.addjob),
    path('submitted',views.submitjob),
    path('pricing',views.price_page),
    path('products',views.product_page),
    path('delete',views.delete_job),
    path('register',views.register),
    path('welcome',views.welcome),
    path('logout',views.logout),
    path('login',views.login),
    path('admin',views.admin)

]