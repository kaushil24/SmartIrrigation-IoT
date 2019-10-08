from django.contrib import admin

# Register your models here.
from .models import TempSensor as ts
from .models import HumiditySensor as hs 
from .models import MoistureSensor as ms
from .models import Motor as m

admin.site.register(ts)
admin.site.register(hs)
admin.site.register(ms)
admin.site.register(m)