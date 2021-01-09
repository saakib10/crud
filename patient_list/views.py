from django.shortcuts import render,HttpResponseRedirect
from .forms import DetailsInput
from .models import PatientDetails

def add_view(request):
    if request.method == 'POST':
        rm = DetailsInput(request.POST)
        if rm.is_valid():
            rm.save()
        rm = DetailsInput()
    else:
        rm = DetailsInput()
    pati = PatientDetails.objects.all()
    return render(request, 'form.html', {'form' : rm , 'pat' : pati })

def delete_data(request,id):
    if request.method == 'POST':
        pi = PatientDetails.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pa = PatientDetails.objects.get(pk=id)
        pi = DetailsInput(request.POST, instance = pa)
        if pi.is_valid():
            pi.save()

        else:
          pa = PatientDetails.objects.get(pk=id)
          pi = DetailsInput(instance=pa)
    return render(request,'update.html',{'form' : pi })
