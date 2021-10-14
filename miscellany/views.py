from django.shortcuts import render
from .models import GithubRepo, Myself, Skill
from .forms import reachout
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    title='Home'
    profile=Myself.objects.all()
    skills=Skill.objects.all()
    repos=GithubRepo.objects.all()

    if request.method == 'POST':
        form = reachout(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            reach_out = form.save(commit=False)
            reach_out.save()
        return redirect('home')
    else:
        form = reachout()

    return render(request, 'index.html', {'title': title, 'myself': profile, 'skills': skills, 'repos': repos, 'form':form})