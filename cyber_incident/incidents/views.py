from django.shortcuts import render
from django.http import HttpResponse
from .models import Incident
from django.shortcuts import redirect

def home(request):
    if request.method=="POST":
        title=request.POST.get('title',"").strip()
        description=request.POST.get('description',"").strip()
        
        if title and description:
            Incident.objects.create(title=title,description=description)
        return redirect('home')
    
    # Create your views here.
    incidents=Incident.objects.all()
    return render(request,'incidents/home.html',{'incidents':incidents})
