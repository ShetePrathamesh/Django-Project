from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import MedicineForm
from .models import Medicine

# Create your views here.

def add(request):
    form = MedicineForm(request.POST or None)

    if form.is_valid():    
        form.save()  
    return render(request,'add.html',{'form':form})

def show(request):
    medicine = Medicine.objects.all()
    return render(request,'show.html',{'medicine':medicine})

def update(request,Id):
    medicine = Medicine.objects.get(Id=Id)
    form = MedicineForm(request.POST or None, instance = medicine)
    if form.is_valid():    
        form.save()
        return HttpResponseRedirect("/")
    return render(request,'update.html',{'medicine':medicine})

def delete(request,Id):
    medicine = Medicine.objects.get(Id=Id)
    medicine.delete()
    return HttpResponseRedirect("/")