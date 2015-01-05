#coding:utf-8
from django.db import models

class s1(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)