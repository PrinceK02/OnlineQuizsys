from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model
User=get_user_model()

CHOICES1= [
    ('CS', 'Computer Science'),
    ('IT', 'Information Technology'),
    ('Civil', 'Civil'),
    ('Mechanical', 'Mechanical'),
    ('EC', 'Electronics & Communication'),
    ('EEE', 'Electrical & Electronics Engg.'),
    ('EE', 'Electrical Engg.'),
    ('IC', 'Instrumentation & Control Engg.'),
    ]

CHOICES2 = [
	('Student','Student'),
	('Teacher','Teacher'),
]

class signup_form(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"defaultForm-name"}))
	branch=forms.CharField(widget=forms.Select(choices=CHOICES1,attrs={"class":"multiple","id":"defaultForm-college"}))
	contact=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"defaultForm-contact"}))
	year=forms.IntegerField(label="Year(Min=1,Max=4)",validators=[MinValueValidator(1),MaxValueValidator(4)],widget=forms.NumberInput(attrs={"class":"form-control","id":"defaultForm-year"}))
	college=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"defaultForm-college"}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","id":"defaultForm-email"}))
	password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={"class":"form-control","id":"defaultForm-password"}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"defaultForm-confirm_pass"}))
	user = forms.CharField(widget=forms.Select(choices=CHOICES2,attrs={"class":"multiple","id":"defaultForm-user"}))


	def clean_email(self):
		email=self.cleaned_data.get("email")
		qs=User.objects.filter(username=email)
		if qs.exists():
			raise forms.ValidationError("Email Taken !")
		elif ("@" not in email) or (".com" not in email):
			raise forms.ValidationError("Please Enter a Valid Email !")
		return email


	
	# def clean(self):
	# 	data=self.cleaned_data
	# 	password=self.cleaned_data.get("password")
	# 	password1=self.cleaned_data.get("confirm_password")
	# 	if password1 != password:
	# 		raise forms.ValidationError("Password must Match !")
	# 	return data

	def clean_confirm_password(self):
		data=self.cleaned_data
		print(data)
		password=self.cleaned_data.get('password')
		password1=self.cleaned_data.get('confirm_password')
		if password1!=password:
			raise forms.ValidationError("Password must Match !!")
		return data


class login_form(forms.Form):
	email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"defaultForm-email"}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"defaultForm-pass"}))
	user = forms.CharField(widget=forms.Select(choices=CHOICES2,attrs={"class":"multiple","id":"defaultForm-user"}))