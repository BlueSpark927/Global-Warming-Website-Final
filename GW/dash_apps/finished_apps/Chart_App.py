import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from GW.models import Months

item = Months.objects.all().values()
df0 = pd.DataFrame(item)


df0['Year']= df0['Year'].map(str)


app = DjangoDash('Chart_App')

app.layout = html.Div([

    html.H1("Average Maximum and Minimum Temperature in Fahrenheit by Month and State", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "1979", "value": "1979"},
                     {"label": "1980", "value": "1980"},{"label": "1981", "value": "1981"},
                     {"label": "1982", "value": "1982"},{"label": "1983", "value": "1983"},
                     {"label": "1984", "value": "1984"},{"label": "1985", "value": "1985"},
                     {"label": "1986", "value": "1986"},{"label": "1987", "value": "1987"},
                     {"label": "1988", "value": "1988"},{"label": "1989", "value": "1989"},
                     {"label": "1990", "value": "1990"},{"label": "1991", "value": "1991"},
                     {"label": "1992", "value": "1992"},{"label": "1993", "value": "1993"},
                     {"label": "1994", "value": "1994"},{"label": "1995", "value": "1995"},
                     {"label": "1996", "value": "1996"},{"label": "1997", "value": "1997"},
                     {"label": "1998", "value": "1998"},{"label": "1999", "value": "1999"},
                     {"label": "2000", "value": "2000"},{"label": "2001", "value": "2001"},
                     {"label": "2002", "value": "2002"},{"label": "2003", "value": "2003"},
                     {"label": "2004", "value": "2004"},{"label": "2005", "value": "2005"},
                     {"label": "2006", "value": "2006"},{"label": "2007", "value": "2007"},
                     {"label": "2008", "value": "2008"},{"label": "2009", "value": "2009"},
                     {"label": "2010", "value": "2010"},{"label": "2011", "value": "2011"},
                 ],
                 multi=False,
                 value="2000",
                 style={'text-align': 'center'}
                 ),
    dcc.Dropdown(id="slct_month",
                 options=[
                     {"label": "Jan", "value": "Jan"},
                     {"label": "Feb", "value": "Feb"},
                     {"label": "Mar", "value": "Mar"},
                     {"label": "Apr", "value": "Apr"},
                     {"label": "May", "value": "May"},
                     {"label": "Jun", "value": "Jun"},
                     {"label": "Jul", "value": "Jul"},
                     {"label": "Aug", "value": "Aug"},
                     {"label": "Sep", "value": "Sep"},
                     {"label": "Oct", "value": "Oct"},
                     {"label": "Nov", "value": "Nov"},
                     {"label": "Dec", "value": "Dec"},
                 ],
                 multi=False,
                 value="Jan",
                 style={'text-align': 'center'}
                 ),

    html.Div(id='output_container', children=[],style={'text-align': 'center'}),
    html.Br(),

    dcc.Graph(id='map', figure={})

])


# ------------------------------------------------------------------------------

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_month', component_property='value'),
     Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd1, option_slctd2):
    print(option_slctd1, option_slctd2)
    print(type(option_slctd1),type(option_slctd2))

    container = "{}".format(option_slctd2) + " {}".format(option_slctd1)

    dff = df0.copy()
    dff = dff[dff["Month"] == option_slctd1]
    dff = dff[dff["Year"] == option_slctd2]
    
    
    # Plotly 
    fig=go.Figure(data=[
    go.Bar(name='Max', x=dff['State'], y=dff['Max']),
    go.Bar(name='Min', x=dff['State'], y=dff['Min'])


    
    ])
    fig.update_layout(barmode='group')
    
    return container, fig
