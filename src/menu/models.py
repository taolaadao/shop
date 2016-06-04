from __future__ import unicode_literals

from django.db import models

# Create your models here.
class cat(models.Model):
	cat_name=models.CharField(max_length=200)
	cat_type= models.CharField(max_length=200)

	def __unicode__(self):
	    return self.cat_name

	def __str__(self):
		return self.cat_name					


class menu(models.Model):
	name=models.CharField(max_length=200)
	des=models.TextField(max_length=20000)
	price=models.FloatField()
	publish= models.DateTimeField(auto_now_add=True)
	draft=models.BooleanField(default=0)
	cat= models.ForeignKey(cat)


	def __unicode__(self):
	    return self.name

	def __str__(self):
		return self.name					
	def get_absolute_url(self):
		return "detail/%s/" %(self.id)