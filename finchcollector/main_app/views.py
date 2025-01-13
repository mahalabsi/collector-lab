from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Finch
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import VisitForm

class FinchCreate(CreateView):
    model = Finch
    fields = ['name','breed', 'description','age', 'image']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description','age']
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def finch_index(request):
    finches=Finch.objects.all()
    return render(request, 'finches/index.html',{'finches':finches})
def finches_detail(request, finch_id):
    finch= Finch.objects.get(id=finch_id)
    visit_form = VisitForm
    return render(request, 'finches/detail.html',{'finch':finch, 'visit_form': visit_form})
def add_visit(request, finch_id):
    form = VisitForm(request.POST)
    if form.is_valid():
        new_visit = form.save(commit=False)
        new_visit.finch_id = finch_id
        new_visit.save()
    return redirect('detail', finch_id = finch_id)