from bokeh.plotting import figure, output_file, show, ColumnDataSource, save  # figure for plots, output html file, show
from bokeh.models.tools import HoverTool # for tooltips
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral10
import pandas as pd

df = pd.read_csv('C:/Users/16049/Documents/HtN2021/trainingSet.csv')

source = ColumnDataSource(df)

# data list
sentiment_list = df.sentiment.to_list()
withhold_list = df.withhold.to_list()
title_list = df.title.to_list()

source = ColumnDataSource(data = dict(
    x=sentiment_list,
    y=withhold_list,
    desc=title_list

))

output_file('clickfait_training_data_visualization.html')

p = figure(
    title="Clickfait - Training Data Sample",
    plot_width=800,
    plot_height=600,
    x_axis_label="Sentiment",
    y_axis_label="Withholding Information"
)

p.xaxis.axis_label_text_font_size = "15pt"
p.yaxis.axis_label_text_font_size = "15pt"
p.title.text_font_size = '25pt'
p.title.align = 'center'

hover = HoverTool()
hover.tooltips = [
    ("Title", "@desc"),
    ("Sentiment", "$x"),
    ("Withholding Information", "$y")
]
p.add_tools(hover)

p.circle('x', 'y', size=8, color='navy', alpha=0.7, source=source)

show(p)





