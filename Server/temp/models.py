from django.db import models

class Temp(models.Model):

	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add = True)
	parent = models.CharField(max_length=100, default="Adruino UNO")
	data = models.FloatField(default = -1.0)
	unit = models.CharField(max_length = 10, default = "'C")
	anamoly = models.BooleanField(default=False)

	def __str__(self):
		return ("Temperature" + str(self.data))
