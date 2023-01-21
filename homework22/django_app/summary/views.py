from django.shortcuts import render

def index(request):
    return render(request, 'home.html', {})
    
def skills(request):
    return render(request, 'skills.html', {})


def education(request):
    return render(request, 'education.html', {})