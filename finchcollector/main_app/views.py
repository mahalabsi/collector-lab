from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Finch, Home
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 

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

#Homes
class HomeList(ListView):
    model= Home

class HomeDetail(DetailView):
    model=Home

class HomeCreate(CreateView):
    model=Home
    fields= '__all__'

class HomeUpdate(UpdateView):
    model=Home
    fields=['type', 'color']

class HomeDelete(DeleteView):
    model=Home
    success_url='/homes/'




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
    homes_finch_doesnt_have = Home.objects.exclude(id__in = finch.homes.all().values_list('id'))
    return render(request, 'finches/detail.html',{'finch':finch, 'visit_form': visit_form, 'homes':homes_finch_doesnt_have})



def add_visit(request, finch_id):
    form = VisitForm(request.POST)
    if form.is_valid():
        new_visit = form.save(commit=False)
        new_visit.finch_id = finch_id
        new_visit.save()
    return redirect('detail', finch_id = finch_id)

def assoc_home(request, finch_id, home_id):
    #toys is the m:m field name
    Finch.objects.get(id=finch_id).homes.add(home_id)
    return redirect('detail', finch_id = finch_id)

def unassoc_home(request, finch_id, home_id):
    #toys is the m:m field name
    Finch.objects.get(id=finch_id).homes.remove(home_id)
    return redirect('detail', finch_id = finch_id)
