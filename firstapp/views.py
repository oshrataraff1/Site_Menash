from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from firstapp.models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion, ContactFormLog, Blog
from django.template.loader import render_to_string
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    
    general_info = GeneralInfo.objects.first()
    
    
    services = Service.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    recent_blogs = Blog.objects.all().order_by("-created_at")[:3]
    testimonials = Testimonial.objects.all()
    for t in testimonials:
        t.star_range = range(t.rating_count)    
    
    deafult_value = ""
    context = {
        "company_name" : getattr(general_info, "company_name", deafult_value),
        "location" : getattr(general_info, "location", deafult_value), 
        "email" : getattr(general_info, "email", deafult_value),  
        "phone" : getattr(general_info, "phone", deafult_value), 
        "open_hours" : getattr(general_info, "open_hours", deafult_value), 
        "video_url" : getattr(general_info, "video_url", deafult_value), 
        "twitter_url" : getattr(general_info, "twitter_url", deafult_value), 
        "facebook_url" : getattr(general_info, "facebook_url", deafult_value), 
        "instagram_url" : getattr(general_info, "instagram_url", deafult_value), 
        "linkedin_url" : getattr(general_info, "linkedin_url", deafult_value), 
        
        "services" : services,
        "testimonials" : testimonials,
        "faqs" : faqs,
        "recent_blogs": recent_blogs,
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
        
        is_success = False
        is_erorr = False
        erorr_message = ""
        
        try:
            send_mail(
                subject = subject,
                message = None,
                html_message = html_content,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [settings.EMAIL_HOST_USER,], #'exploter@gmail.com'
                fail_silently = False, #default is True    
            )
        except Exception as e:
            is_erorr = True
            erorr_message = str(e)
            messages.error(request,'There was an erorr, could not send E-mail')
        else:
            is_success = True
            messages.success(request,'E-mail has been sent')
            
        ContactFormLog.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message,
                action_time = timezone.now(),
                is_success = is_success,
                is_erorr = is_erorr,
                erorr_message = erorr_message,
        )
    return redirect('app')


def blog_deatail(request, blog_id):
    
    blog = Blog.objects.get(id=blog_id)
    recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:2]
    
    context= {
        "blog": blog,
        "recent_blogs": recent_blogs,
    }
    
    return render(request, "blog_deatails.html", context)

def blogs(request):
    all_blogs = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(all_blogs, 2)  # 3 blogs per page

    # Get the page number from the request GET parameters
    page_number = request.GET.get('page')
    # Retrieve that specific page (or the first page if `page_number` is None)
    page_obj = paginator.get_page(page_number)
    
    # print("Page number:", page_obj.number)
    # print("Total pages:", page_obj.paginator.num_pages)
    # print("Has next?:", page_obj.has_next())
    # print("Items on this page:", len(page_obj.object_list))
    

    context = {
        # The full queryset if you need it:
        "all_blogs": all_blogs,
        # The paginated page of blogs:
        "page_obj": page_obj,
    }
    return render(request, "blogs.html", context)
    
