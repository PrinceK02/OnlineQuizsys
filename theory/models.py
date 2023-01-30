from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import decorators
# Create your models here.
class Quest(models.Model):
    title = models.TextField(null = True, blank = True)
    desc = models.TextField(null = True, blank = True, max_length = 10000)
    #choices = models.ForeignKey('Queries.Choice', on_delete = models.CASCADE)
    status = models.CharField(default = 'inactive',max_length = 10)
    entered_by = models.ForeignKey(User, null = True, blank = True, on_delete = models.CASCADE)
    start_date = models.DateTimeField(null = True, blank = True)
    end_date = models.DateTimeField(null = True, blank = True)
    create_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class Answers(models.Model)   :
    pass


    
