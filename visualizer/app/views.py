from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from api.forms import OOP_Form

# Create your views here.
def index(request):
    return render(request, "app/index.html", {"OOP_Form" : OOP_Form})