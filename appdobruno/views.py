from django.shortcuts import render, redirect, get_object_or_404
from .models import Sports, Routine, Activities
from .forms import SportsForm, ActivitiesForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  sports= Sports.objects.all()
  routine= Routine.objects.all()
  activities= Activities.objects.all()
  return render(request, "home.html",context={"esportes":sports,"rotina":routine,"atividades":activities})

@login_required
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

@login_required
def delete_sport(request, slug):
    sport = get_object_or_404(Sports, slug=slug)
    if request.method == 'POST':
        sport.delete()
        return redirect("home")
  
    return render(request, 'delete_sports.html', {'sport': sport})

@login_required
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

@login_required
def delete_activity(request, slug):
    activity = get_object_or_404(Activities, slug=slug)
    if request.method == 'POST':
        activity.delete()
        return redirect("home")
  
    return render(request, 'delete_activity.html', {'activity': activity})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")