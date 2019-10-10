from django.contrib import admin
from .models import Temp

class table(admin.ModelAdmin):
	list_display = ('date','time', 'temperature', 'moisture', 'humidity', 'parent','anamoly')



admin.site.register(Temp, table)
# admin.site.unregister(Language)
admin.site.site_header = "Full Marks Please"
