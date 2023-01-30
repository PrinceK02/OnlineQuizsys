from django.shortcuts import render, redirect
from .forms import compilerForm
from django.template.backends.django import DjangoTemplates
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
import requests
import json
# Create your views here.

def index(request):
    form = compilerForm()
    return render(request,"mycompiler/index.html",{'form':form,'title':'Compiler!'})


def execute(request):
    if request.method == "POST":
        form = compilerForm(request.POST)
        if form.is_valid():
            inp = form.cleaned_data['inputArea']
            #oup = exec(inp)
            language = form.cleaned_data['language']
            vI = form.cleaned_data['version']
            payload = {"clientId":"9583a02cf6e53497a4ecea8ad7b7f424","clientSecret":"aecfecefad5209437415aa51649420aa5ab4b4fd7b041d591964e2e9db475fdc","script":inp,"language":language,"versionIndex":vI}
            headers = {'content-type':'application/json'}
            result = requests.post("https://api.jdoodle.com/v1/execute",data=json.dumps(payload),headers=headers)
            properres = json.loads(result.text)
            return render(request,"mycompiler/index.html",{'form':form,'title':'Compiler!','iA':properres.get('output')})    
    else:
        return HttpResponse("Not Done!")

def compilersoption(request):
    return render(request,'mycompiler/compilers.html')
