from django import forms

class SendEmailForm(forms.Form):
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required = True)
    
