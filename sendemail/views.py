from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SendEmailForm

def emailView(request):
    if request.method == 'GET':
        form = SendEmailForm()
    else:
        form = SendEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            to_email = form.cleaned_data['to_email']
            message = form.cleaned_data['message']
            send_mail(subject, message,'pyappmedia@gmail.com', [to_email,], fail_silently = False)
            return redirect('success')
    return render(request, "sendemail/email.html", {'form': form})

def successView(request):
    return render(request, "sendemail/success.html")
