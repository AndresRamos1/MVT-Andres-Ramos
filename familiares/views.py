from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def familia(request):
    return render(request, "familia.html")