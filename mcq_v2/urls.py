"""mcq_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import sendmail,SRemoveQuiz,TRemoveQuiz,information,EditStudent,EditTeacher,AddtoList,DeleteQuestion,EditQuestion,AddQuestion,AddQuiz,deleteQuiz,editQuiz,index,login_view,signup,instruction,dashboard,leaderboard,logout_view,result,teacher



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('signup/',signup),
    path('login/',login_view),
    path('logout/',logout_view,name="logout"),
    path('information/',information,name="information"),
    path('leaderboard/',leaderboard),
    path('teacher/',teacher),
    path('editteacher/',EditTeacher,name="EditTeacher"),
    path('editstudent/',EditStudent,name="EditStudent"),

    #quiz
    path('instruction/<int:id>',instruction, name="AttemptQuiz"),
    path('SRemoveQuiz/<int:id>',SRemoveQuiz,name="SRemoveQuiz"),
    path('TRemoveQuiz/<int:id>/<int:user1>/<int:lbpk>',TRemoveQuiz,name="TRemoveQuiz"),
    path('dashboard/<int:id>',dashboard,name="dashboard"),
    path('result/<int:id>',result,name="result"),
    path('mail/<int:id>',sendmail,name="sendmail"),
    path('addQuiz',AddQuiz,name="addQuiz"),
    path('editQuiz/<int:id>',editQuiz,name="editQuiz"),
    path('deleteQuiz/<int:id>',deleteQuiz,name="deleteQuiz"),
    path('AddtoList/<int:id>',AddtoList,name="AddtoList"),

    #question
    path('addQuestion',AddQuestion,name="AddQuestion"),
    path('EditQuestion/<int:id1>/<int:id2>',EditQuestion,name="EditQuestion"),
    path('DeleteQuestion/<int:id1>/<int:id2>',DeleteQuestion,name="DeleteQuestion"),
    # path('email/',include('sendemail.urls')),
    #path('contact/',include('contactus.urls')),
    # path('theory/',include('theory.urls')),
    # path('editor/',include('editor.urls')),
    # path('compiler/',include('mycompiler.urls')),
    #path('theory/<int:id>',include('theory.urls')),
]
