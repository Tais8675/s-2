from django.shortcuts import render
from .models import App, Lista

# Create your views here.

def index(request):
    return render(request, "app/index.html", {
        "app": App.objects.all()
    })

def app(request, app_id):
    app = app.objects.get(id=app)
    return render(request, "app/pag.html", {
        "app": App
    })
