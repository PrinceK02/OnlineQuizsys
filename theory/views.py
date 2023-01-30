from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import *
from theory.models import Quest
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url="/login/")
def index(request):
    context = {}
    questions= Quest.objects.all()#query sent to the database
    context['title'] = 'Subjective Queries'
    context['questions'] = questions
    return render(request,"theory/theory.html",context)

def details(request,id):
    context = {}
    question = Quest.objects.get(id=id)
    description = Quest.objects.get()
    #choice = Choice.objects.all)
    context['question'] = question
    context['description'] = description
    return render(request, 'theory/one.html',context)
