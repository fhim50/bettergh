from django.db import models
from django.contrib import admin
# Create your models here.

class Name(models.Model):
	name = models.CharField(max_length = 100)
	
	
	class Meta:
		db_table = 'names'
	
	def __unicode__(self):
		return self.name
		
		
class NameAdmin(admin.ModelAdmin):
	search_fields = ('Names',)
	
	pass

admin.site.register(Name, NameAdmin )