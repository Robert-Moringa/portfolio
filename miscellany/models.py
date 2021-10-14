from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GithubRepo(models.Model):
    name = models.TextField(max_length=200, null=True, blank=True, default="name")
    project_landing = models.ImageField(upload_to='Project_images/', null=True, blank=True)
    about = models.TextField()
    project_link=models.URLField(max_length=250)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        db_table = 'skills'

    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ContactMe(models.Model):
    class Meta:
        db_table = 'contact_me'

    name= models.CharField(max_length=40)
    company_name= models.CharField(max_length=40)
    description=models.TextField()
    email=models.EmailField()
    skills=models.ForeignKey(Skill, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Which of my skills are you interested in?')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Myself(models.Model):
    class Meta:
        db_table='myself'

    name=models.CharField(max_length=40)
    about=models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    email= models.EmailField()
    edit_date = models.DateTimeField(auto_now_add=True)
    skills= models.ForeignKey(Skill, null=True, blank=True, on_delete=models.CASCADE)
    repos=models.ForeignKey(GithubRepo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name