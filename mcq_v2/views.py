from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import signup_form,login_form
from quiz.models import quizze
from quiz_qus.models import question
from random import shuffle
from leaderboard.models import leaderboard as lb
from userprofile.models import sprofile
from teacher.models import tprofile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
import math


from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()


def index(request):
	if request.POST:
		print(request.POST)
	return render(request,'index/index.html',{})



def signup(request):
	form_class=signup_form(request.POST or None)
	context={
		"form":form_class
	}
	if form_class.is_valid():
		name=form_class.cleaned_data.get("name")
		email=form_class.cleaned_data.get("email")
		college=form_class.cleaned_data.get("college")
		year=form_class.cleaned_data.get("year")
		branch=form_class.cleaned_data.get("branch")
		password=form_class.cleaned_data.get("password")
		contact=form_class.cleaned_data.get("contact")
		uselect=form_class.cleaned_data.get("user")
		new_user= User.objects.create_user(email,email,password)
		if uselect == "Student":
			user_profile=sprofile(
					user=new_user,
					name=name,
					college=college,
					year=year,
					branch=branch,
					contact=contact,
					status=uselect,
				)
			user_profile.save()
			messages.success(request,"Your account "+ str(user_profile.user) +" for student has been created successfully.")
		elif uselect == "Teacher":
			teacher_profile=tprofile(
					user=new_user,
					name=name,
					college=college,
					year=year,
					contact=contact,
					status=uselect,
				)
			teacher_profile.save()
			messages.success(request,"Your account "+ str(teacher_profile.user) + " for teacher has been created successfully.")
		if new_user is not None:
			return redirect("/login")
	return render(request,'signup/signup.html',context)



def login_view(request):
	form_class=login_form(request.POST or None)
	content={
		"form": form_class
	}
	if request.method=="POST":
		if form_class.is_valid():
			username=form_class.cleaned_data.get("email")
			password=form_class.cleaned_data.get("password")
			status=form_class.cleaned_data.get("user")
			user = authenticate(username=username, password=password)
			if user is not None:
				if status=="Teacher":
					try:
						teacher=tprofile.objects.get(user=user)
					except tprofile.DoesNotExist:
						messages.info(request,"Please enter valid cridentials.")
						return redirect('/login')
					login(request,user)
					messages.info(request,"You are now logged in as "+str(username))					
					return redirect('/teacher')
				elif status=="Student":
					try:
						student=sprofile.objects.get(user=user)
					except sprofile.DoesNotExist:
						messages.info(request,"Please enter valid cridentials.")
						return redirect('/login')
					login(request,user)
					messages.info(request,"You are now logged in as "+str(username))
					return redirect('/information')
			else:
				messages.info(request,"Please enter valid cridentials.")
				return redirect('/login')
	return render(request,'login/login.html',content)


@login_required
def teacher(request):
	teacher=tprofile.objects.get(user=request.user)
	quiz_object = list(quizze.objects.all())
	quescount=[]
	quiztime=[]
	for quiz in quiz_object:
		quescount.append(quiz.ques.all().count())
		if(quiz.time>=60):
			hours=quiz.time//60
			minutes=quiz.time%60
			time=str(hours)+" hour "+str(minutes)+" minutes"
			quiztime.append(time)
		else:
			time=str(quiz.time)+" minutes"
			quiztime.append(time)
	multivalue=zip(quiz_object,quescount,quiztime)
	print(multivalue)
	leaderboard=list(lb.objects.all())
	users=list(sprofile.objects.all())
	lead=[]
	stud=[]
	for student in users:
		for lbs in leaderboard:
			if(lbs.user==student.user):
				stud.append(student)
				lead.append(lbs)
	multivalue1=zip(stud,lead)
	context = {
		'Teacher':teacher,
		'multivalue':multivalue,
		'multivalue1':multivalue1,
		# 'Quiz':quiz_object,
		# 'quescount':quescount,
	}
	return render(request,'teacher/teacher.html',context)

@login_required
def information(request):
	student=sprofile.objects.get(user=request.user)
	if student.start_time==0:
		quiz_object = list(quizze.objects.all())
		quescount=[]
		quiztime=[]
		for quiz in quiz_object:
			quescount.append(quiz.ques.all().count())
			if(quiz.time>=60):
				hours=quiz.time//60
				minutes=quiz.time%60
				time=str(hours)+" hour "+str(minutes)+" minutes"
				quiztime.append(time)
			else:
				time=str(quiz.time)+" minutes"
				quiztime.append(time)
		multivalue=zip(quiz_object,quescount,quiztime)
		
		attempted=list(student.quizes.all())
		lbpks=[] #pk of leaderboards.
		lbquizes=[] # quiz names of leaderboards.
		lbs=lb.objects.filter(user=request.user)
		for leaderboard in lbs:
			for attquez in attempted:
				if leaderboard.quiz==attquez:
					lbpks.append(leaderboard.pk)
					lbquizes.append(leaderboard.quiz)
		multivalue2=zip(lbquizes,lbpks)
		context={
			'Student':student,
			'Attemptedlb':multivalue2,
			'multivalue':multivalue,
		}
		return render(request,'student/information.html',context)
	else:
		student.start_time=0
		student.save()
		logout(request)
		messages.info(request,"You have been logged out due to unethical activity.")
		return redirect('/login')

@login_required
def SRemoveQuiz(request,id):
	student=sprofile.objects.get(user=request.user)
	lbs=lb.objects.filter(user=request.user)
	quizes=list(student.quizes.all())
	for quiz in quizes:
		if quiz.pk==id:
			for lbobject in lbs:
				if lbobject.quiz==quiz:
					lbobject.delete()
					print('deleted')
			student.quizes.remove(quiz)
			messages.success(request,quiz.title+" has been removed.")

	
	return redirect('/information')

@login_required
def TRemoveQuiz(request,id,user1,lbpk):
	student=sprofile.objects.get(pk=user1)
	print(student.name)
	lbs=lb.objects.get(pk=lbpk)
	
	quizes=list(student.quizes.all())
	for quiz in quizes:
		if quiz.pk==id:
			if lbs.quiz==quiz:
				lbs.delete()
			student.quizes.remove(quiz)
			messages.success(request,quiz.title+" has been removed.")

	
	return redirect('/teacher')

@login_required
def instruction(request,id):
	student=sprofile.objects.get(user=request.user)
	if student.start_time==0:
		quiz=quizze.objects.get(pk=id)
		totalQ=quiz.ques.all().count()
		time=""
		maxmarks=quiz.ques.all().count()
		if(quiz.time>=60):
				hours=quiz.time//60
				minutes=quiz.time%60
				time=str(hours)+" hour "+str(minutes)+" minutes"
		else:
			time=str(quiz.time)+" minutes"
		
		context={
			'quiz':quiz,
			'quiztime':time,
			'maxmarks':maxmarks*4,
			'totalQ':totalQ,
		}
		return render(request,'test/instruction.html',context)
	else:
		student.start_time=0
		student.save()
		logout(request)
		messages.info(request,"You have been logged out due to unethical activity.")
		return redirect('/login')

def dashboard(request,id):
	quiz_object=quizze.objects.get(pk=id)
	student=sprofile.objects.get(user=request.user)
	queryset=list(quiz_object.ques.all())
	totalQ=quiz_object.ques.all().count()
	if student.start_time==0:
		student.start_time=1
		student.save()
		shuffle(queryset)
		time=quiz_object.time
		context={
			"totalQ":totalQ,
			"questionset":queryset,
			"time":time
		}
		return render(request,'test/dashboard.html',context)
	else:
		if request.POST:
			student=sprofile.objects.get(user=request.user)
			student.save()
			student.quizes.add(quiz_object)
			student.save()
			count=0
			attempted_qus=0
			for q in queryset:	
				if request.POST.get(str(q.pk))==str(q.correct_option):
					count=count+1		
				if request.POST.get(str(q.pk))==None:  # count unattempted ques.
					attempted_qus=attempted_qus+1
			attempted_qus= totalQ - attempted_qus	# get attempted questions.
			correct_qus=int(count)
			wrong_qus=attempted_qus-count
			points=(correct_qus*4)
			max_marks=totalQ*4
			per = ((points/max_marks)*100)
			if per<=30:
				message="Better luck next time !!"
			elif per>40 and per<=60:
				message="Congrats!! You have Done Pretty well."
			elif per>60 and per<=80:
				message="Congrats!! You have Done your Best."
			else:
				message="Congrats You Rocked !!🎉🎉"

			object_1=lb.objects.filter(user=request.user)	# created if object already present in leaderboard.
			print(object_1)
			for student in object_1:
				if student.quiz==quiz_object:
					print('update existing quiz')
					student.correct_qus=correct_qus
					student.wrong_qus=wrong_qus
					student.points=points
					student.message=message
					student.attempted_qus=attempted_qus
					student.save()
					st=sprofile.objects.get(user=request.user)
					st.start_time=0
					st.save()
					messages.success(request,quiz_object.title+" has been submitted successfully")
					return redirect('/information')

			print('existing user with new leaderboard object')		
			lb1=lb(
				user=request.user,
				quiz=quiz_object,
				correct_qus=correct_qus,
				wrong_qus=wrong_qus,
				points=points,
				message=message,
				attempted_qus=attempted_qus
			)
			lb1.save()
			st=sprofile.objects.get(user=request.user)
			st.start_time=0
			st.save()
			messages.success(request,quiz_object.title+" has been submitted successfully.")
			return redirect('/information')
		student.start_time=0
		student.save()
		logout(request)
		messages.info(request,"You have refreshed the page and have been logged out.")
		return redirect('/login')

@login_required
def result(request,id):
	if request.user.is_authenticated:
		obj=lb.objects.get(pk=id)
		totalQ=obj.quiz.ques.all().count()
		context={
			"lb":obj,
			"totalQ":totalQ*4,
		}
		
		# logout(request)
	# else:
	# 	context_2={}
	return render(request,'test/result.html',context)


@login_required
def sendmail(request,id):
	lb1 = lb.objects.get(pk=id)
	teacher=tprofile.objects.get(user=request.user)
	quiz_object=quizze.objects.get(pk=lb1.quiz.pk)
	totalQ=quiz_object.ques.all().count()
	max_marks = totalQ*4
	per = (lb1.points/max_marks)*100
	per=math.trunc(per)
	if request.method=="POST":
		subject=str(lb1.quiz)+' Result'
		to=str(lb1.user)
		ccTitle=str(request.POST['ccTitle'])
		cc=ccTitle.split(',')
		remarks = request.POST['message']
		from_email='QUIZ SYSTEM <jmitknowledge@gmail.com>'
		image='assets/img/quiz_logo.jpg'
		d={
			'lb':lb1,
			'totalQ':totalQ*4,
			'remarks':remarks,
			'per':per,
			'teacher':teacher,
			'imgpath':image,
		}
		TextBody=render_to_string('email.txt',d)
		HtmlBody=render_to_string('email.html',d)
		msg=EmailMultiAlternatives(subject,TextBody,from_email,[to],cc=cc)
		msg.attach_alternative(HtmlBody,'text/html')
		msg.send()
		messages.info(request,"Result has been sent to respective mail id.")
		return HttpResponse('<script>window.opener.location.reload();window.close();</script>')
	return render(request,'teacher/sendmail.html',{'lb':lb1,'teacher':teacher,})





def leaderboard(request):
	object_1=lb.objects.all().order_by('-points')	# sorting and assigning objects in descending order of their points.
	context={
		"object":object_1
	}
	return render(request,'test/leaderboard.html',context)

@login_required
def EditStudent(request):
	student=sprofile.objects.get(user=request.user)
	context={
		'Student':student,
		'branchlist':student.CHOICES,
	}
	if request.method=="POST":
		name=request.POST['Sname']
		college=request.POST['Scollege']
		branch=request.POST['Sbranch']
		year=request.POST['Syear']
		contact=request.POST['Scontact']

		student.college=college
		student.name=name
		student.branch=branch
		student.year=year
		student.contact=contact
		student.save()
		messages.info(request,"Details Updated")
		return HttpResponse('<script>window.opener.location.reload();window.close();</script>')
	return render(request,'student/EditStudent.html',context)

@login_required
def EditTeacher(request):
	teacher=tprofile.objects.get(user=request.user)
	context={
		'Teacher':teacher,
		'branchlist':teacher.CHOICES,
	}
	if request.method=="POST":
		name=request.POST['Tname']
		college=request.POST['Tcollege']
		branch=request.POST['Tbranch']
		year=request.POST['Tyear']
		contact=request.POST['Tcontact']

		teacher.name=name
		teacher.college=college
		teacher.branch=branch
		teacher.year=year
		teacher.contact=contact
		teacher.save()
		messages.info(request,"Details Updated.")
		return HttpResponse('<script>window.opener.location.reload();window.close();</script>')
	return render(request,'teacher/EditTeacher.html',context)

@login_required
def AddQuiz(request):
	questionset=list(question.objects.all())
	context={
		'quesset':questionset,
	}
	if request.method=="POST":
		title = request.POST['quiz_title']
		time = request.POST['quiz_time']
		questions = request.POST.getlist('questions')
		new_quiz = quizze()
		new_quiz.title=title
		new_quiz.time=time
		new_quiz.save()
		for ques in questionset:
			for que in questions:
				if ques.pk==int(que):
					new_quiz.ques.add(ques)
		messages.success(request,title+" has been added successfully.")
		return HttpResponse('<script>window.opener.location.reload();window.close();</script>')
	return render(request,'teacher/AddQuiz.html',context)

@login_required
def AddQuestion(request):
	if request.method=="POST":
		ques_id=request.POST['ques_id']
		ques_title=request.POST['ques_title']
		ques_desc=request.POST['ques_desc']
		option1=request.POST['option1']
		option2=request.POST['option2']
		option3=request.POST['option3']
		option4=request.POST['option4']
		correct_option=request.POST['correct_option']
		new_question = question(qus_id=ques_id,title=ques_title,desc=ques_desc,option_1=option1,option_2=option2,option_3=option3,option_4=option4,correct_option=correct_option)
		new_question.save()
		return HttpResponse('<script>window.opener.location.reload();window.close();</script>')
	return render(request,'teacher/AddQuestion.html')

@login_required
def EditQuestion(request,id1,id2):
	quiz = quizze.objects.get(pk=id1)
	Question=quiz.ques.get(pk=id2)
	context={
		'Question':Question,
	}
	if request.method=="POST":
		ques_id=request.POST['ques_id']
		ques_title=request.POST['ques_title']
		ques_desc=request.POST['ques_desc']
		option1=request.POST['option1']
		option2=request.POST['option2']
		option3=request.POST['option3']
		option4=request.POST['option4']
		correct_option=request.POST['correct_option']

		Question.qus_id=ques_id
		Question.title=ques_title
		Question.desc=ques_desc
		Question.option_1=option1
		Question.option_2=option2
		Question.option_3=option3
		Question.option_4=option4
		Question.correct_option=correct_option
		Question.save()
	return render(request,'teacher/EditQuestion.html',context)

@login_required
def DeleteQuestion(request,id1,id2):
	quiz = quizze.objects.get(pk=id1)
	quiz.ques.remove(quiz.ques.get(pk=id2))
	return redirect(reverse(editQuiz,kwargs={'id':id1}))

@login_required
def AddtoList(request,id):
	quiz = quizze.objects.get(pk=id)
	questionset=list(question.objects.all())
	if request.method=="POST":
		questions=request.POST.getlist('questions')
		for ques in questionset:
			for que in questions:
				if ques.pk==int(que):
					quiz.ques.add(ques)
	return redirect(reverse(editQuiz,kwargs={'id':id}))

@login_required
def editQuiz(request,id):
	quiz = quizze.objects.get(pk=id)
	quizQ = quiz.ques.all() # list of question objects in quiz.
	questions = list(question.objects.all()) # list of question objects.
	context={
		'Quiz':quiz,
		'quizQ':quizQ,
		'quesset':questions,
	}

	if request.POST.get('Add')=="AddtoList":
		Questions=request.POST.getlist('questions')
		for ques in questions:
			for que in Questions:
				if ques.pk==int(que):
					quiz.ques.add(ques)
		return redirect(reverse(editQuiz,kwargs={'id':id}))
	elif request.POST.get('Delete')=="DeleteQuestions":
		Questions=request.POST.getlist('questions')
		for ques in questions:
			for que in Questions:
				if ques.pk==int(que):
					ques.delete()
		return redirect(reverse(editQuiz,kwargs={'id':id}))
	elif request.method=="POST":
		quiz_title = request.POST['quiz_title']
		quiz_time = request.POST['quiz_time']
		quiz.title = quiz_title
		quiz.time = quiz_time
		quiz.save()
		messages.info(request,quiz_title+" updated.")
		return HttpResponse('<script>window.opener.location.reload();window.close();</script>')
	return render(request,'teacher/editQuiz.html',context)


@login_required
def deleteQuiz(request,id):
	quiz = quizze.objects.get(pk=id)
	quiz.delete()
	messages.info(request,quiz.title+" deleted")
	return redirect('/teacher')

@login_required
def logout_view(request):
	logout(request)
	messages.success(request,"You have been logged out successfully.")
	return redirect('/')



