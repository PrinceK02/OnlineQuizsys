from django.contrib import admin
from .models import sprofile
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display=['__str__','contact']
	class Meta:
		model=sprofile

admin.site.register(sprofile,BookAdmin)
