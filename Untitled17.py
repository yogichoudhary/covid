#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from datetime import date, timedelta
# !pip install fbprophet
from fbprophet import Prophet


# In[2]:


df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')


# In[82]:


import numpy as np
import datetime
df.head()


# In[83]:


columns = df.columns
print(columns)
letters_index = columns.get_loc("date")
letters_index


# In[84]:


df.head(10)
df['date_']=pd.to_datetime(df['date'])
t=np.min(df['date_'])
q=np.max(df['date_'])

df['time']=df['date_']-t
df['time']=(df['time'] / np.timedelta64(1, 'D')).astype(int)
df['time']


# In[85]:



# df['time']
# initial_visible_month=t + timedelta(days=10)
# # dff['radius']=dff['total_cases']*5000
# initial_visible_month
# df = df[df["date_"]>= initial_visible_month]
# dff['radius']=np.log10(dff['radius'])


# dff['radius']=dff['radius']+0.2
# dff['radius']=dff['radius']*5000
# dff['radius'] = dff['radius'].astype(int) 


# In[98]:


all_location = df.location.unique()

app = dash.Dash(__name__)

#   colors = {
#       'background': '#111111',
#       'text': '#7FDBFF'}
app.layout = html.Div([
    
    
    
    
    dcc.Dropdown(
        id="dropdown_0_1",
        options=[{"label": x, "value": x} 
                 for x in all_location],
        value='World',
#         multi=True,
        style={  
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
       
    ),    
    
        dcc.DatePickerSingle(
        id='my-date-picker-single_1',
        min_date_allowed=t,
        max_date_allowed=q,
        initial_visible_month=q,
        date=q,
        style={   
#             "display": "inline-block",
               "width": "40%",
               'margin-left': '20px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#             'background': '#111111'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
    ),
    
    
    
    html.Div(id='output_container', children=[]),
    html.Div(id='output_container_2', children=[]),
    html.Div(id='output_container_4', children=[]),
    
    
    
    html.Div(id='output_container_1', children=[]),
    html.Div(id='output_container_3', children=[]),
    html.Div(id='output_container_5', children=[]),
    
    
    
    
    
    
    
    dcc.Dropdown(
        id="dropdown_1",
        options=[{"label": x, "value": x} 
                 for x in all_location],
        value='World',
#         style={'width': "40%"}
        style={   
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
    ),
    dcc.Dropdown(
        id="dropdown_1_2",
        options=[{"label": 'Total Cases', "value": columns.get_loc("total_cases")},
                 {"label": 'New Cases', "value": columns.get_loc("new_cases")}, 
#                  {"label": 'total_cases', "value": columns.get_loc("total_cases")}, 
                 {"label": 'Total Deaths', "value": columns.get_loc("total_deaths")}, 
                 {"label": 'New Deaths', "value": columns.get_loc("new_deaths")}, 
#                  {"label": 'Total Cases Per Million', "value": columns.get_loc("total_cases_per_million")}, 
#                  {"label": 'New Cases Per Million', "value": columns.get_loc("new_cases_per_million")}, 
#                  {"label": 'Total Deaths Per Million', "value": columns.get_loc("total_deaths_per_million")}, 
#                  {"label": 'New Deaths Per Million', "value": columns.get_loc("new_deaths_per_million")}, 
                 {"label": 'Total Vaccinations', "value": columns.get_loc("total_vaccinations")}, 
                 {"label": 'People Vaccinated', "value": columns.get_loc("people_vaccinated")}, 
#                 {"label": 'People Vaccinated Per Hundred', "value": columns.get_loc("people_vaccinated_per_hundred")}
           
                 ],      
           
        value=5,
        style={ 
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
    ),
    dcc.Graph(id="line-chart"),
    
    
    dcc.Dropdown(
        id="dropdown_2_1",
        options=[{"label": x, "value": x} 
                 for x in all_location],
        value=['World','India'],
        multi=True,
        style={  
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
       
    ),
    dcc.Dropdown(
        id="dropdown_2_2",
        options=[{"label": 'Total Cases', "value": columns.get_loc("total_cases")},
                 {"label": 'New Cases', "value": columns.get_loc("new_cases")}, 
#                  {"label": 'total_cases', "value": columns.get_loc("total_cases")}, 
                 {"label": 'Total Deaths', "value": columns.get_loc("total_deaths")}, 
                 {"label": 'New Deaths', "value": columns.get_loc("new_deaths")}, 
                 {"label": 'Total Cases Per Million', "value": columns.get_loc("total_cases_per_million")}, 
                 {"label": 'New Cases Per Million', "value": columns.get_loc("new_cases_per_million")}, 
                 {"label": 'Total Deaths Per Million', "value": columns.get_loc("total_deaths_per_million")}, 
                 {"label": 'New Deaths Per Million', "value": columns.get_loc("new_deaths_per_million")}, 
                 {"label": 'Total Vaccinations', "value": columns.get_loc("total_vaccinations")}, 
                 {"label": 'People Vaccinated', "value": columns.get_loc("people_vaccinated")}, 
                {"label": 'People Vaccinated Per Hundred', "value": columns.get_loc("people_vaccinated_per_hundred")}
           
                 ],  
        value=5,
        style={
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
           
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
        
    ),
    html.P(children=' Swith to Logarithmic Scale'),
    
    dcc.RadioItems(
        id="RadioItems_1",
        options=[{"label": 'normal', "value": 1} ,
                 {"label": 'logarithic', "value": 2}],
        value=1,
        style={  
            "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
       
#         labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="line-chart_2",style={   

            
            'background': '#111111'

              }),
    
#     dcc.Dropdown(
#         id="dropdown_3_1",
#         options=[{"label": 'total_cases', "value": 4}, 
#                  {"label": 'new_cases', "value": 5},
#                  {"label": 'new_cases_smoothed', "value": 6},
#                  {"label":'total_deaths', "value": 7},
#                  {"label": 'new_deaths', "value": 8},
#                  {"label": 'new_deaths_smoothed', "value": 9},
#                  ],
#         value=5,
#         style={'width': "40%"}),
        
#     dcc.Slider(
#         id='my-slider',
#         min=t,
#         max=q,
#         step=s,
#         value=r,
#     ),
    dcc.Dropdown(
        id="dropdown_3_1",
       options=[{"label": 'Total Cases', "value": columns.get_loc("total_cases")},
                 {"label": 'New Cases', "value": columns.get_loc("new_cases")}, 
#                  {"label": 'total_cases', "value": columns.get_loc("total_cases")}, 
                 {"label": 'Total Deaths', "value": columns.get_loc("total_deaths")}, 
                 {"label": 'New Deaths', "value": columns.get_loc("new_deaths")}, 
                 {"label": 'Total Cases Per Million', "value": columns.get_loc("total_cases_per_million")}, 
                 {"label": 'New Cases Per Million', "value": columns.get_loc("new_cases_per_million")}, 
                 {"label": 'Total Deaths Per Million', "value": columns.get_loc("total_deaths_per_million")}, 
                 {"label": 'New Deaths Per Million', "value": columns.get_loc("new_deaths_per_million")}, 
                 {"label": 'Total Vaccinations', "value": columns.get_loc("total_vaccinations")}, 
                 {"label": 'People Vaccinated', "value": columns.get_loc("people_vaccinated")}, 
                {"label": 'People Vaccinated Per Hundred', "value": columns.get_loc("people_vaccinated_per_hundred")}
           
                 ],  
        value=4,
        style={   
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#             'background': '#111111'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
        ),
        
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=t,
        max_date_allowed=q,
        initial_visible_month=date(2020, 5, 12),
        date=date(2020, 5, 12),
        style={   
#             "display": "inline-block",
               "width": "40%",
               'margin-left': '20px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#             'background': '#111111'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
    ),
    
    dcc.Graph(id="line-chart_3"),

dcc.Dropdown(
        id="dropdown_4_1",
        options=[{"label": x, "value": x} 
                 for x in all_location],
        value='World',
       
        style={  
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
       
    ),
    dcc.Dropdown(
        id="dropdown_4_2",
        options=[{"label": 'Total Cases', "value": columns.get_loc("total_cases")},
                 {"label": 'New Cases', "value": columns.get_loc("new_cases")}, 
#                  {"label": 'total_cases', "value": columns.get_loc("total_cases")}, 
                 {"label": 'Total Deaths', "value": columns.get_loc("total_deaths")}, 
                 {"label": 'New Deaths', "value": columns.get_loc("new_deaths")}, 
                 {"label": 'Total Cases Per Million', "value": columns.get_loc("total_cases_per_million")}, 
                 {"label": 'New Cases Per Million', "value": columns.get_loc("new_cases_per_million")}, 
                 {"label": 'Total Deaths Per Million', "value": columns.get_loc("total_deaths_per_million")}, 
                 {"label": 'New Deaths Per Million', "value": columns.get_loc("new_deaths_per_million")} 
#                  {"label": 'Total Vaccinations', "value": columns.get_loc("total_vaccinations")}, 
#                  {"label": 'People Vaccinated', "value": columns.get_loc("people_vaccinated")}, 
#                 {"label": 'People Vaccinated Per Hundred', "value": columns.get_loc("people_vaccinated_per_hundred")}
           
                 ],  
            
        value=5,
        style={
#             "display": "inline-block",
               "width": "50%",
               'margin-left': '10px',
               'margin-right': 'auto',
                "verticalAlign": "top"
#                'horizontalAlign':'centre'
           
#                ,'lineHeight': "60px","boederStyle'': "dashed",'borderRadius': "5px"
#                ,‘textAlign’: ‘center’,‘margin’: ‘10px’
#      'borderWidth': "1px"   
              }
        ),
        
            dcc.Graph(id="line-chart_4",style={           
            'background': '#111111'
              }),
 
])


# In[105]:


@app.callback(
    Output("line-chart", "figure"),
    Output("line-chart_2", "figure"), 
    Output("line-chart_3", "figure"),
    Output(component_id='output_container', component_property='children'),
    Output(component_id='output_container_1', component_property='children'),
    Output(component_id='output_container_2', component_property='children'),
    Output(component_id='output_container_3', component_property='children'),
    Output(component_id='output_container_4', component_property='children'),
    Output(component_id='output_container_5', component_property='children'),
    Output("line-chart_4", "figure"),
    [Input("dropdown_1", "value")],
    [Input("dropdown_1_2", "value")],
    [Input("dropdown_2_1", "value")],
    [Input("dropdown_2_2", "value")],
    [Input("RadioItems_1", "value")],
    [Input("dropdown_3_1", "value")],
    [Input("my-date-picker-single", 'date')],
    [Input("dropdown_0_1", "value")],
    [Input("my-date-picker-single_1", 'date')],
    [Input("dropdown_4_1", "value")],
    [Input("dropdown_4_2", "value")]
#     [dash.dependencies.Input('my-slider', 'value')]
#     [Input("dropdown_3_1", "value")]
)
def update_line_chart(location,column,location_2,column_2,log_,column_3,q,o,d,location_3,column_4):
    dff = df.copy()
    
    cases=dff.iloc[1:,column]
    dff['cases'] = cases 
    
    dff = dff[dff["location"] == location].head(1000)
   
    fig1 = px.bar(dff, 
        x="date", y='cases',width=1510, height=500
#                   ,marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',marker_line_width=1.5, opacity=0.6
                 )
    fig1.update_layout(
        title=" ",
        xaxis_title="Time",
        yaxis_title=" ",
        
        plot_bgcolor='rgb(254,254,254)',
#         backgroundColor:='rgb(46,46,46)',
#     legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
#         legend_title_font_color="green"
    ))

    
    
#     if values == []:
#          for val in location_2:
#     location_2 = dff["location"].location_2[0]
 
    i=0
    for val in location_2:
        dff_2 = df.copy()
        dff=dff_2
        cases=dff.iloc[1:,column_2]
        dff['cases'] = cases 
        dff = dff[dff["location"]==val].head(1000)    
        if log_ == 1:
            dff['cases']=dff['cases']
        elif log_ == 2:
            dff = dff[dff["cases"]>=100]
            dff['cases']=np.log10(dff['cases'])
            
        i=i+1
        if i==1:
            fig2=px.line(dff, x="date", y='cases',width=1510, height=700,color='location')
        else:
            fig2.add_scatter(x=dff['date'], y=dff['cases'], mode='lines',name=location_2[i-1])
#         fig2.append(fig)
    fig2.update_xaxes(rangeslider_visible=True)
    fig2.update_layout(
        title=" ",
        xaxis_title="Time",
        yaxis_title=" ",
        
        plot_bgcolor='rgb(254,254,254)',
#     legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
#         legend_title_font_color="green"
    ))
    dff = df.copy()
    dff.dropna(subset=['continent'], inplace=True)
    cases=dff.iloc[1:,column]
    dff['cases'] = cases 
   
    
    dff['date_']= pd.to_datetime(dff['date'])
    cases=dff.iloc[1:,column_3]
    dff['cases'] = cases
    dff = dff[dff["date_"]== q]
    n=np.max(dff['cases'])
    r=np.min(dff['cases'])
#     dff['radius']=dff['total_cases']*5000
#     dff['radius']=np.log10(dff['radius'])
#     dff['radius']=dff['radius']+0.2
#     dff['radius']=dff['radius']*5000
#     dff['radius'] = dff['radius'].astype(int) 
    fig3 = px.choropleth(dff, locations="iso_code",
                    color="cases", # lifeExp is a column of gapminder
                    hover_name="location", # column to add to hover information
#                     color_continuous_scale=px.colors.sequential.Plasma
                         color_continuous_scale="Viridis",
                        range_color=(r, n),
                         title="Choropleth Map",
                        height=900
                     
                         
                        )
#     fig3 = px.line(dff, x="date", y='cases',width=1510, height=500,color='location')
    
    dff = df.copy()
    data=[]
    dff = dff[dff["location"]==o].head(1000)    
    dff['date_']= pd.to_datetime(dff['date'])
    dff = dff[dff["date_"]== d]
    container = "Total Cases: {}".format(dff.iloc[0,columns.get_loc("total_cases")])
    container1 = "New Cases: {}".format(dff.iloc[0,columns.get_loc("new_cases")])
    container2 = "Total Deaths: {}".format(dff.iloc[0,columns.get_loc("total_deaths")])
    container3 = "New Deaths: {}".format(dff.iloc[0,columns.get_loc("new_deaths")])
    container4 = "Total Vaccination: {}".format(dff.iloc[0,columns.get_loc("total_vaccinations")])
    container5 = "New Vaccination: {}".format(dff.iloc[0,columns.get_loc("new_vaccinations")])
    
    
    
    
    
    
    dff = df.copy()
    df2=dff[dff['location']==location_3]
    cases=df2.iloc[1:,column_4]
    df2['cases'] = cases
    df3 = pd.DataFrame()
    df3['ds']=df2['date_'] 
    df3['y']=df2['cases']
    m = Prophet(interval_width=0.95)
    m.fit(df3)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    df4 = pd.DataFrame()
    df4['ds']=forecast['ds']
    df4['yhat']=forecast['yhat']
    df4=df4[df4['ds']>datetime.datetime(2020, 12, 31)]
    fig4=px.line(df3, x="ds", y='y',width=1510, height=700)
    fig4.add_scatter(x=df4['ds'], y=df4['yhat'], mode='lines',name='predicted')
    fig4.update_xaxes(rangeslider_visible=True)
    fig4.update_layout(
        title=" ",
        xaxis_title="Time",
        yaxis_title=" ",
        
        plot_bgcolor='rgb(254,254,254)',
#     legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
#         legend_title_font_color="green"
    ))
    
    
    return fig1,fig2,fig3,container,container1,container2,container3,container4,container5,fig4







# In[ ]:


if __name__ == '__main__':
    app.run_server(port = 8787)


# In[105]:


# df.head(10)
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[283]:
#
#
# dfff=df[df['location']=='India']
# dfff=dfff[dfff['date_']==q]
# dfff.iloc[0,columns.get_loc("total_cases")]
#
#
# # In[ ]:
#
#
#
#
#
# # In[101]:
#
#
#
#
#
# # In[132]:
#
#
# #     dff_3 = df.copy()
# #     dff=dff_3
# #     dff['date_']= pd.to_datetime(dff['date'])
# #     cases=dff.iloc[1:,5]
# #     dff['cases'] = cases
# #     dff = dff[dff["date_"] == q].head(1000)
# #     dff['radius']=dff['total_cases']*5000
#
# #     dff['radius']=np.log10(dff['radius'])
# #     dff['radius']=dff['radius']+0.2
# #     dff['radius']=dff['radius']*5000
# #     dff['radius'] = dff['radius'].astype(int)
# #     fig3 = px.scatter_geo(dff, locations="iso_code", color="location", hover_name="total_cases", size="radius", projection="natural earth")
#
#
# # In[87]:
#
#
# # dff = df
#
#
# # dff['date_']= pd.to_datetime(dff['date'])
# # t=np.min(dff['date_'])
# # q=np.max(dff['date_'])
# # # cases=dff.iloc[1:,5]
# # # dff['cases'] = cases
# # # dff = dff[dff["date_"]>= t + timedelta(days=100)]
# # dff = dff[dff["date_"]== q - timedelta(days=100)]
# # # t=np.min(dff['date_'])
# # # dff['time']=dff['date_']-(q - timedelta(days=100))
# # # dff['time']=dff['time'] / np.timedelta64(1, 'D')
# # df['total_cases_']=np.log10(df['total_cases'])
#
# # #     dff['radius']=dff['total_cases']+8
# # #     dff['radius']=np.log10(dff['radius'])
# # #     dff['radius']=dff['radius']+0.2
# # #     dff['radius']=dff['radius']*5000
# # #     dff['radius'] = dff['radius'].astype(int)
# # fig = px.scatter_geo(dff, locations="iso_code", color="location",
# #                      hover_name="location", size="total_cases",
# # #                      animation_frame="date_",
# #                      projection="natural earth"
# #                     )
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[54]:
#
#
# df2=df[df['location']=='World']
#
#
# # In[55]:
#
#
# df2['date_']= pd.to_datetime(df2['date'])
#
#
# # In[56]:
#
#
# df3 = pd.DataFrame()
# df3['ds']=df2['date_']
# df3['y']=df2['new_cases']
# df3=df3
#
#
# # In[57]:
#
#
# m = Prophet(interval_width=0.95)
# m.fit(df3)
# future = m.make_future_dataframe(periods=7)
# future.tail()
# forecast = m.predict(future)
#
#
# # In[58]:
#
#
# df4 = pd.DataFrame()
# df4['ds']=forecast['ds']
# df4['yhat']=forecast['yhat']
# df4=df4[df4['ds']>datetime.datetime(2021, 1, 1)]
# fig4=px.line(df3, x="ds", y='y',width=1510, height=700)
# fig4.add_scatter(x=df4['ds'], y=df4['yhat'], mode='lines',name='predicted')
#
#
# # In[10]:
#
#
#
#
#
# # In[14]:
#
#
# df4=df4[df4['ds']>datetime.datetime(2021, 1, 1)]
#
#
# # In[15]:
#
#
# df4
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
#
# # In[ ]:
#
#
#
#
