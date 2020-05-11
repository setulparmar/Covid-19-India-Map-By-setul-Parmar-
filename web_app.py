import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import folium

app=dash.Dash(__name__)
server=app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout=html.Div(style={'backgroundColor': colors['background']},[html.H1('Covid19-India-Map(By Setul Parmar)',style={'color':'#FBABAB'}),html.H5('These numbers are only shown state wise and not district wise.',style={'color':colors['text']}),html.H5('The First and Second number denotes Total cases and Recovered cases of respective states.',style={'color':colors['text']}),html.H6('Source:https://www.mohfw.gov.in/',style={'color':colors['text']}),html.Iframe(id='map',srcDoc=open('Covid19India.html','r').read(),width='100%',height='580'),html.H4('Updated on:10 May 2020',style={'color':colors['text']})])

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
if __name__=='__main__':
    app.run_server(debug=True)
