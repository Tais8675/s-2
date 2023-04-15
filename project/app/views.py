from django.shortcuts import render
from .models import App, Lista

# Create your views here.

def index(request):
    return render(request, "app/index.html", {
        "app": App.objects.all()
    })

def app(request, app_id):
    app = App.objects.get(id=app_id)
    return render(request, "app/pag.html", {
        "app": App
    })
