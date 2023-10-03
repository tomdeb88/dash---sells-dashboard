from dash import dcc,html
import pandas as pd
import plotly.graph_objects as go
from dash import dcc,html,dash
import app


def render_tab(df):
    x=df[df['total_amt']>0].groupby([pd.Grouper(key='tran_date',freq='C'),'Store_type'])['total_amt'].sum().round(2).unstack()
    
    
    bars = []
    for col in x.columns:
        bars.append(go.Bar(x=x.index.day_name().unique(),y=x[col],name=col,hoverinfo='text',
        hovertext=[ f'{y} $' for y in x[col]]))

    data = bars
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack'))

    

    layout=html.Div(children=[html.Div([html.H1('Sprzedaz wedlug dni tygodnia',style={'font-size':'35px','margin-bottom':'30px'}),
                                        dcc.Graph(id='days_graph',figure=fig,style={'height':'600px'})],style={'width':"50%"}),
                                        html.Div([html.H1('Charakterystyka kupujacych',style={'font-size':'35px'}),
                                                  html.Br(),html.Div([dcc.RadioItems([i for i in df['Store_type'].unique()], 'Flagship store',id='radio',inline=True),
                                                                      dcc.Graph(figure={},id='histogram',style={'height':'570px'})])],style={'width':'50%'})
                            
                              ],style={'display':'flex','padding-top':'30px','text-align':'center'})
       
 

    return layout