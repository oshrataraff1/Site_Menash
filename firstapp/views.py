from django.shortcuts import render
from firstapp.models import GeneralInfo, Service, Testimonial


# Create your views here.

def index(request):
    
    general_info = GeneralInfo.objects.first()
    
    
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    for t in testimonials:
        t.star_range = range(t.rating_count)    
    
    context = {
        "company_name" : general_info.company_name,
        "location" : general_info.location,
        "email" :  general_info.email,
        "phone" :  general_info.phone,
        "open_hours" : general_info.open_hours,
        "video_url" : general_info.video_url,
        "twitter_url" : general_info.twitter_url,
        "facebook_url" :  general_info.facebook_url,
        "instagram_url" : general_info.instagram_url,
        "linkedin_url" : general_info.linkedin_url,
        
        "services" : services,
        "testimonials" : testimonials,
    }
    
    return render(request, "index.html", context)

def index_personal(request):
    
    general_info = GeneralInfo.objects.first()
    
    services = Service.objects.all()
    
    context = {
        "company_name" : general_info.company_name,
        "location" : general_info.location,
        "email" :  general_info.email,
        "phone" :  general_info.phone,
        "open_hours" : general_info.open_hours,
        "video_url" : general_info.video_url,
        "twitter_url" : general_info.twitter_url,
        "facebook_url" :  general_info.facebook_url,
        "instagram_url" : general_info.instagram_url,
        "linkedin_url" : general_info.linkedin_url,
        
        "services" : services,
    }
    return render(request, "index-personal.html", context)
