from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Character, Place, Option
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings

# Create your views here.


def index(request):
	if request.user.is_authenticated:
		return render(request, "index.html")
	return redirect("register")


def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password1")
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect("index")
	else:
	    form = UserCreationForm()

	return render(request, "registration/registration.html", {"form": form})


@login_required
def place(request, id):
	char = Character.objects.get(id=id)
	if char not in request.user.characters.all():
		return HttpResponseForbidden()
	if char.place is None:
		place = Place.objects.get(name=settings.START_PLACE)
	else:
		place = char.place

	return render(request, "place.html", {"place": place, "character": char})
