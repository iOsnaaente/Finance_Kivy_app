from kivy.lang import Builder

from kivymd.tools.hotreload.app import MDApp

from kivy.utils import platform
if platform == 'win':
    from kivy.core.window import Window
    Window.size = (435, 700)
    import os 
    PATH = os.path.dirname( __file__ )

from kivy.clock import Clock
import numpy as np 
from scipy.interpolate import make_interp_spline 
import matplotlib.pyplot as plt 
import matplotlib as mpl 

from widgets.kivyplt import MatplotFigure


from kivy.properties import StringProperty, NumericProperty, ColorProperty, ObjectProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton 

class PieGraph( MDFloatLayout ):
    bd_widget_color = ColorProperty()
    bd_pie_color = ColorProperty()
    legend_text_color = ColorProperty()
    labels  = ListProperty()
    values  = ListProperty()
    colors  = ListProperty()
    explodes = ListProperty()
    show_percent = False
    show_labels = False
    legend  = False     
    radius_in = 0.5
    radius_out = 1 
    border = 0.05

    def __init__(
            self, 
            values, 
            colors, 
            labels = [], 
            explodes = [], 
            bd_widget_color = 'white', 
            bd_pie_color = 'white', 
            show_labels = False, 
            show_percent = False,
            legend = False, 
            legend_text_color = 'black', 
            *args, **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self.legend_text_color = legend_text_color
        self.bd_widget_color = bd_widget_color
        self.bd_pie_color = bd_pie_color
        self.show_labels = show_labels
        self.show_percent = show_percent
        self.legend = legend
        self.labels = labels
        self.values = values
        self.colors = colors
        self.explodes = explodes
        if not explodes: 
            self.explodes = [ 0.0 for _ in range(len(values))] 
        if len(values) == len(colors):
            Clock.schedule_once( self.draw_pie_chart, .1 )

    def set_radius(self, r_in, r_out):
        self.radius_in = r_in
        self.radius_out = r_out

    def set_border(self, border):
        self.border = border 

    def draw_pie_chart( self, _ ):
        bd_out_circle = plt.Circle( (0, 0), self.radius_out + self.border, fc = self.bd_pie_color )
        bd_in_circle  = plt.Circle( (0, 0), self.radius_in, fc = self.bd_pie_color )
        center_circle = plt.Circle( (0, 0), self.radius_in - self.border, fc = self.bd_widget_color)

        chart = mpl.figure.Figure( )
        # bd_color      = plt.Rectangle( (0,0), self.ids.graph_here.width, self.ids.graph_here.height, fc = self.bd_widget_color  )
        # chart.gca().add_artist( bd_color )
        chart.gca().add_artist( bd_out_circle )

        if not self.show_labels:
            chart.gca().pie(
                self.values, 
                colors = self.colors, 
                labels = self.labels if self.show_labels else [ '' for _ in range(len(self.values)) ],  
                autopct = '%1.1f%%' if self.show_percent else '',
                pctdistance = 0.85, 
                explode = self.explodes
                ) 

        chart.gca().add_artist( bd_in_circle )
        chart.gca().add_artist( center_circle )
        
        plot = MatplotFigure( chart )

        if self.legend == True: 
            self.legend_zone.size_hint = [0.4, 1]
            self.legend_zone.pos_hint = {'right': 1,'center_y': 0.5}
            self.graph_zone.size_hint  = [0.6, 1]
            self.graph_zone.pos_hint = {'left': 1,'center_y': 0.5}
        else: 
            self.legend_zone.size_hint = [0, 1]
            self.graph_zone.size_hint  = [1, 1]
            self.graph_zone.pos_hint = {'center_x': 0.5,'center_y': 0.5}
        
        self.ids.graph_zone.add_widget( plot )

        for color, label in zip(self.colors, self.labels):
            self.legend_zone.add_widget(
                MDRectangleFlatIconButton(
                    icon = "circle",
                    text = label,
                    theme_text_color = "Custom",
                    text_color = self.legend_text_color,
                    line_color = [0,0,0,0],
                    theme_icon_color = "Custom",
                    icon_color = color
                )
            )
            


labels   = [ 'Aluguel', 'Condominio', 'Internet','Gás', 'Carro']
values   = [ 1240, 160, 75, 120, 700]
colors   = [ '#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500']
# explodes = ( 0.05, 0.05, 0.05, 0.05, 0.05)

class Graph(MDApp):
    KV = PATH + '\\graph.kv'
    DEBUG = True  
    KV_FILES = [PATH + "\\graph.kv"]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self):
        self.PAGE = Builder.load_file(self.KV)
        self.PAGE.ids.graph_box.add_widget(
            PieGraph(
                labels   = labels,
                values   = values,
                colors   = colors,
                # explodes = explodes,
                legend   = True,
                # bd_widget_color = [1,1,0,1], 
                bd_pie_color = [.65,0.5,1,1]
            )
        )
        return self.PAGE


Graph().run()





def chart( ):
    chart = mpl.figure.Figure( figsize = (2,2) )
    x = np.array( [ x for x in range(10) ] )
    y = [ 0, 600, 400, 100, 500, 1000, 750, 400, 1000, 100 ]
    xlabels = [ str(i) for i in range(10) ]
    ny = []
    for e in y:
        if e not in ny:
            ny.append(e)
    ny.sort()
    ylabels = [ 'R$' + str(i) for i in ny ] 
    chart.gca().set_xticklabels( xlabels )
    chart.gca().set_yticklabels( ylabels )
    xy_spline = make_interp_spline( x, y )
    x1 = np.linspace( x.min(), x.max(), 500 )
    y1 = xy_spline(x1)
    chart.gca().spines['top'].set_visible(False)
    chart.gca().spines['right'].set_visible(False)
    chart.gca().spines['left'].set_visible(False)
    chart.gca().plot(x1, y1)
    plot = MatplotFigure( chart )
    # self.PAGE.ids.graph_box.clear_widgets()
    # self.PAGE.ids.graph_box.add_widget( plot )



