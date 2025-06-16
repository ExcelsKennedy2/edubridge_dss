from django.shortcuts import render

def base(request):
    return render(request, 'core/base.html')

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def category(request):
    return render(request, 'core/category.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')

def job_detail(request):
    return render(request, 'core/job-detail.html')

def job_list(request):
    return render(request, 'core/job-list.html')

def error(request):
    return render(request, 'core/404.html')