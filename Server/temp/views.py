from django.shortcuts import render
from rest_framework import viewsets
from .models import Temp
from .serializers import TempSerializer
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
import numpy as np




class TempView(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer


def graph1(request, *arge, **kwargs):

	df = pd.DataFrame(list(Temp.objects.values()))

	TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
]

	p1 = figure(x_axis_type="datetime", title="Temperature Variations", tooltips = TOOLTIPS)
	p1.grid.grid_line_alpha=0.3
	p1.xaxis.axis_label = 'Date'
	p1.yaxis.axis_label = '`C'

	# p1.line(np.array(df['date'], dtype=np.datetime64), df['temperature'], color='#A6CEE3', legend='AAPL')
	p1.line(df['time'], df['temperature'], color='#A6CEE3', legend='Temp', line_width = 3)
	p1.legend.location = "top_left"
	sc1, div1 = components(p1)

	p2 = figure(x_axis_type='datetime', tooltips = TOOLTIPS)
	p2.line(df['time'], df['humidity'], color='#B2DF8A', legend='Humid', line_width = 3)
	# p1.line(datetime(IBM['date']), IBM['adj_close'], color='#33A02C', legend='IBM')
	# p1.line(datetime(MSFT['date']), MSFT['adj_close'], color='#FB9A99', legend='MSFT')
	sc2, div2 = components(p2)

	p3 = figure(x_axis_type='datetime', tooltips = TOOLTIPS)
	p3.line(df['time'], df['moisture']/50, color='black', legend='Moisture', line_width = 1)
	# p1.line(datetime(IBM['date']), IBM['adj_close'], color='#33A02C', legend='IBM')
	# p1.line(datetime(MSFT['date']), MSFT['adj_close'], color='#FB9A99', legend='MSFT')
	sc3, div3 = components(p3)

	

    # print('ssd')

	return render(request, 'graph1.html', {'sc1': sc1, 'div1':div1, 'sc_hum': sc2, 'div_hum': div2, 'sc_mos': sc3, 'div_mos': div3}) 

