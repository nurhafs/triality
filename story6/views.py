from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Activity, Participant
from .forms import Par_Form, Act_Form

# Create your views here.
def act(request):
    keg = Activity.objects.all()
    keg_form = Act_Form(request.POST or None)
    response = {'kegiatan' : keg,
                'a_form': keg_form}
    if request.method == 'POST':
        if keg_form.is_valid():
            keg.create(
                actname=keg_form.cleaned_data.get('actname')
            )
    return render(request, 'kegiatan.html', response)

def peserta(request, par_id):
    allp = Activity.objects.get(id = par_id)
    peserta = Participant.objects.all()
    form = Par_Form(request.POST or None)
    response = {'parti' : allp,
                'peserta' : peserta,
                'par_form' : form }
    if request.method=='POST':
            if form.is_valid():
                peserta.create(
                name=form.cleaned_data.get('name'),
                contact_number=form.cleaned_data.get('contact_number'),
                activity=allp
                )
    return render(request, 'people.html', response)

def delact(request, kp):
    obj = Activity.objects.get(id = kp)
    obj.delete()
    return HttpResponseRedirect('/activity/')
