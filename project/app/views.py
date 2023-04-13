from django.shortcuts import render
from .models import app, lista

# Create your views here.

def index(request):
    return render(request, "app/index.html", {
        "app": app.objects.all()
    })

def app(request, app_id):
    app = app.objects.get(id=app)
    return render(request, "app/pag.html", {
        "app": app
    })
