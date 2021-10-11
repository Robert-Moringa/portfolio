from django.contrib import admin
from .models import GithubRepo,Skill,Myself,ContactMe

# Register your models here.
admin.site.register(GithubRepo)
admin.site.register(Skill)
admin.site.register(Myself)
admin.site.register(ContactMe)
