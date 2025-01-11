from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="Company")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        db_table = "general_company_info"
        
        
        
class Service(models.Model):
    bootstrap_icon = models.CharField(max_length=100, blank=True, null=True)
    fontawsome_icon = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "company_services"
    
class Testimonial(models.Model):
    user_image = models.CharField(max_length=255, blank=True, null=True)
    stars_count =[
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField(choices=stars_count)
    username = models.CharField(max_length=50)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()
    
    def __str__(self):
        return f"{self.username} - {self.user_job_title}"
    
    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_erorr = models.BooleanField(default=False)
    erorr_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.email
    
    
class Author(models.Model):
    
    author_pic = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.first_name
            
    
class Blog(models.Model):
    blog_image = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    #on_delete=models.CASCADE - if deleting the author, django will auto delete the author's blogs
    #on_delete=models.PROTECT - when trying to delete the author, Django will not allow it if the author has blogs
    #on_delete=models.SET_NULL - if deleting the author, django will make the author column as blank (requires to have the null=True & blank=True attributes)
    created_at = models.DateTimeField(default=timezone.now)
    content = RichTextField() # models.TextField()
    
    def __str__(self):
        return self.title
       
