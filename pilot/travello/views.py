from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = "Nairobi"
    dest1.desc = "Kesho tuko maandamano"
    dest1.price = 1000

    dest2 = Destination()
    dest2.name = "Mombasa"
    dest2.desc = "Zakayo lazima atashuka"
    dest2.price = 800
    return render(request, "index.html", {'dest1': dest1, "dest2": dest2})

