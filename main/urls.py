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
    path('jobs', views.jobs_display),
    path('deletejob',views.delete_job)
]