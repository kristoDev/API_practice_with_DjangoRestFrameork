# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models




# Create your models here.
class Status(models.Model):

	user		= models.ForeignKey
	content		= models.TextField(nul=True, blanc=True)
	image		= models.imageField(nul=True, blanc=True)
	update		= models.DateTimeField(auto_add_now=True, nul=True, blanc=True)
	timestamp	= models.DateTimeField(auto_add_now=True, nul=True, blanc=True)

	def __str__(self):
		return str(self.content)[:50]

	
		