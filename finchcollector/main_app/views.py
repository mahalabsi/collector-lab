from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Finch, Home
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from .forms import VisitForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class FinchCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = ['name','breed', 'description','age', 'image']
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

class FinchUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = ['breed', 'description','age']
class FinchDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url = '/finches/'

#Homes
class HomeList(LoginRequiredMixin, ListView):
    model= Home

class HomeDetail(LoginRequiredMixin, DetailView):
    model=Home

class HomeCreate(LoginRequiredMixin, CreateView):
    model=Home
    fields= '__all__'

class HomeUpdate(LoginRequiredMixin, UpdateView):
    model=Home
    fields=['type', 'color']

class HomeDelete(LoginRequiredMixin, DeleteView):
    model=Home
    success_url='/homes/'




def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

@login_required
def finch_index(request):
    # finches=Finch.objects.all()
    finches=Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html',{'finches':finches})


@login_required
def finches_detail(request, finch_id):
    finch= Finch.objects.get(id=finch_id)
    visit_form = VisitForm
    homes_finch_doesnt_have = Home.objects.exclude(id__in = finch.homes.all().values_list('id'))
    return render(request, 'finches/detail.html',{'finch':finch, 'visit_form': visit_form, 'homes':homes_finch_doesnt_have})


@login_required
def add_visit(request, finch_id):
    form = VisitForm(request.POST)
    if form.is_valid():
        new_visit = form.save(commit=False)
        new_visit.finch_id = finch_id
        new_visit.save()
    return redirect('detail', finch_id = finch_id)

@login_required
def assoc_home(request, finch_id, home_id):
    #toys is the m:m field name
    Finch.objects.get(id=finch_id).homes.add(home_id)
    return redirect('detail', finch_id = finch_id)

@login_required
def unassoc_home(request, finch_id, home_id):
    #toys is the m:m field name
    Finch.objects.get(id=finch_id).homes.remove(home_id)
    return redirect('detail', finch_id = finch_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Signup- Please try again later.'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)