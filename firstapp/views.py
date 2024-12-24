from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from firstapp.models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    
    general_info = GeneralInfo.objects.first()
    
    
    services = Service.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
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
        "faqs" : faqs,
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


def contact_form(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print("\nUser have submitted a form\n")
        
        context = {
            "name" : name,
            "email" : email,
            "subject" : subject,
            "message" : message,
        }
        
        html_content = render_to_string('email.html', context)
        
        send_mail(
            subject = subject,
            message = None,
            html_message = html_content,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.EMAIL_HOST_USER,], #'exploter@gmail.com'
            fail_silently = False, #default is True    
        )
        
    return redirect('app')
