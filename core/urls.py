from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category', views.category, name='category'),
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/', views.job_detail, name='job-detail'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error, name='404'),
]