from django.db import models
from datetime import date

# Create your models here.

class TempSensor(models.Model):

	date = models.DateField(default=date.today)
	time = models.TimeField(auto_now_add = True)
	parent = models.CharField(max_length=100, default="Adruino UNO")
	data = models.FloatField(default = -1.0)
	unit = models.CharField(max_length = 10, default = "'C")
	anamoly = models.BooleanField(default=False)


class HumiditySensor(models.Model):

	date = models.DateField(default = date.today)
	time = models.TimeField(auto_now_add=True)
	parent = models.CharField(max_length=100, default="Adruino UNO")
	data = models.FloatField(default = -1.0)
	unit = models.CharField(max_length = 10, default = "%")
	anamoly = models.BooleanField(default=False)


class MoistureSensor(models.Model):

	date = models.DateField(default = date.today)
	time = models.TimeField(auto_now_add=True)
	parent = models.CharField(max_length=100, default="Adruino UNO")
	data = models.FloatField(default = -1.0)
	unit = models.CharField(max_length = 10, default = "%")
	anamoly = models.BooleanField(default=False)


class Motor(models.Model):

	activation = models.BooleanField(default=False)
	activationTime = models.TimeField(auto_now = True)
	activationDate = models.DateField(auto_now=True)

