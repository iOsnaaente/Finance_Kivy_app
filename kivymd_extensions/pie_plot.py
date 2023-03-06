from kivy.properties import ColorProperty, ListProperty
from kivymd.uix.button import MDRectangleFlatIconButton 
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np 

from kivyplt import MatplotFigure
from kivy.clock import Clock

KV_PIE_PLOT = '''
<PieGraph>:
    graph_zone:graph_zone
    legend_zone:legend_zone
    MDBoxLayout: 
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        orientation: 'horizontal'
        MDBoxLayout:
            id: graph_zone
            size_hint: 0.7, 1
            pos_hint: {'left': 1,'center_y': 0.5}
        MDBoxLayout:
            id: legend_zone
            size_hint_x: 0.3                  
            orientation: 'vertical'
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
'''


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
    border = 0.01
    def __init__(
            self, 
            values : list , 
            colors : list , 
            labels = [], 
            explodes = [], 
            bd_widget_color = 'white', 
            bd_pie_color = 'white', 
            show_labels = False, 
            show_percent = False,
            legend = False, 
            legend_font_size = 14,
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
        self.legend_font_size = legend_font_size
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
        if len(self.values) == len(self.colors):
            Clock.schedule_once( self.draw_pie_chart, .1 )

    def set_border(self, border):
        self.border = border         
        if len(self.values) == len(self.colors):
            Clock.schedule_once( self.draw_pie_chart, .1 )


    def draw_pie_chart( self, _ ):
        bd_out_circle = plt.Circle( (0, 0), self.radius_out + self.border, fc = self.bd_pie_color )
        bd_in_circle  = plt.Circle( (0, 0), self.radius_in, fc = self.bd_pie_color )
        center_circle = plt.Circle( (0, 0), self.radius_in - self.border, fc = self.bd_widget_color)

        chart = mpl.figure.Figure( )
        # bd_color = plt.Rectangle( (0,0), self.ids.graph_here.width, self.ids.graph_here.height, fc = self.bd_widget_color  )
        # chart.gca().add_artist( bd_color )
        
        chart.gca().add_artist( bd_out_circle )
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
            self.graph_zone.size_hint  = [0.6, 1]
        else: 
            self.legend_zone.size_hint = [0, 1]
            self.graph_zone.size_hint  = [1, 1]
        
        self.ids.graph_zone.clear_widgets()
        self.ids.graph_zone.add_widget( plot )

        if self.legend:
            self.ids.legend_zone.clear_widgets()
            for color, label in zip(self.colors, self.labels):
                self.legend_zone.add_widget(
                    MDRectangleFlatIconButton(
                        icon = "circle",
                        size_hint_x = 1,
                        text = label,
                        font_size = self.legend_font_size,
                        icon_size = str(self.legend_font_size) + 'sp',
                        theme_text_color = "Custom",
                        text_color = self.legend_text_color,
                        line_color = [0,0,0,0],
                        theme_icon_color = "Custom",
                        icon_color = color
                    )
                )
            self.ids.legend_zone.adaptive_height = True
