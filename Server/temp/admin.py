from django.contrib import admin
from .models import Temp

class table(admin.ModelAdmin):
	list_display = ('date','time', 'temperature', 'moisture', 'humidity', 'parent','anamoly')
	list_filter = ('date',)
	change_list_template = 'admin/temp/temp_change_list.html'



admin.site.register(Temp, table)
# admin.site.unregister(Language)
admin.site.site_header = "Full Marks Please"
