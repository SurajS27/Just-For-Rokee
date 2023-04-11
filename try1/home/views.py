from dataclasses import dataclass
from django.shortcuts import render
from subprocess import run,PIPE
import sys
# Create your views here.
def index(request):
    return render(request,"index.html")

def op(request):
    return render(request,"opsub.html")

def sim(request):
    return render(request,"sim.html")

def simres(request):
    z1 = int(request.GET["z1"])
    z2 = int(request.GET["z2"])
    x1 = int(request.GET["x1"])
    y1 = int(request.GET["y1"])
    c1 = int(request.GET["c1"])
    x2 = int(request.GET["x2"])
    y2 = int(request.GET["y2"])
    c2 = int(request.GET["c2"])

    res = z1+z2+x1+y1+c1+x2+y2+c2

    return render(request, 'simres.html', {'simres':res})










