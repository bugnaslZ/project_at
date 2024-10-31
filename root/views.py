from django.shortcuts import render
from .models import Testmonials,Fqa,service,service_two , Pros , Prices
# Create your views here.
def home(request):
    testmonials = Testmonials.objects.all()
    fqas = Fqa.objects.all()
    services = service.objects.filter(status=True)
    services_two = service_two.objects.filter(status=True)
    pross = Pros.objects.filter(status = True)
    prices = Prices.objects.filter(status= True) 
    return render(request,'root/index.html',context={'testmonials':testmonials,'fqas':fqas,'services':services,'services_two':services_two,'pross':pross,'prices':prices})
