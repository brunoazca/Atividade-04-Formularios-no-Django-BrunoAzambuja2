from django.shortcuts import render, redirect, get_object_or_404
from .models import Sports, Routine, Activities
from .forms import SportsForm, ActivitiesForm

# Create your views here.
def home(request):
  sports= Sports.objects.all()
  routine= Routine.objects.all()
  activities= Activities.objects.all()
  return render(request, "home.html",context={"esportes":sports,"rotina":routine,"atividades":activities})

def add_or_edit_sport(request, slug=None):
    if slug:
        sport = get_object_or_404(Sports, slug=slug)
    else:
        sport = None
    
    if request.method == 'POST':
        form = SportsForm(request.POST, instance=sport)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SportsForm(instance=sport)
    
    return render(request, 'sports_form.html', {'form': form})
  
def delete_sport(request, slug):
    sport = get_object_or_404(Sports, slug=slug)
    if request.method == 'POST':
        sport.delete()
        return redirect("home")
  
    return render(request, 'delete_sports.html', {'sport': sport})

def add_or_edit_activity(request, slug=None):
    if slug:
        activity = get_object_or_404(Activities, slug=slug)
    else:
        activity = None
    
    if request.method == 'POST':
        form = ActivitiesForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ActivitiesForm(instance=activity)
    
    return render(request, 'activities_form.html', {'form': form})
  
def delete_activity(request, slug):
    activity = get_object_or_404(Activities, slug=slug)
    if request.method == 'POST':
        activity.delete()
        return redirect("home")
  
    return render(request, 'delete_activity.html', {'activity': activity})

