# app.title='ERI Research Dashboard'

# def get_options(list_of_pis):
#     dict_list = []
#     for i in list_of_pis:
#         dict_list.append({'label': i, 'value': i})
#     return dict_list.sort()

# list_of_years = df['year'].unique().tolist()
# list_of_years.sort(reverse=True)

# fig.update_layout(xaxis_showgrid=False, 
#                   yaxis_showgrid=False, 
#                   xaxis_zeroline=False, 
#                   yaxis_zeroline=False, 
#                   yaxis_visible=False, 
#                   xaxis_visible=False)

# fig.update_layout(legend_title='Main Topic', legend= {'itemsizing': 'constant'})),

# dcc.Dropdown(id="pi-selector",
 #    options=get_options(df['Name'].unique()),
 #    value=[df['Name'].sort_values()[0]],
 #    style={'backgroundColor': '#1E1E1E'},
 #    className='pi-selector')
	# options=[
	# {"label": i, "value": i} for i in list_of_pis],
	# value='Kelly Caylor', 
	# multi=False,
	# placeholder="Select a PI",
	# )

# html.Div(
# 	className="div-for-dropdown",
        #     children=[
        #         # Dropdown to select years
        #         dcc.Dropdown(
        #             id="year-selector",
        #             options=[
        #                 {"label": i, "value": i} for i in list_of_years],
        #             value=df['year'].max(),
        #             multi=False,
        #             placeholder="Select a year",
        #         )
        #     ],
        # ),


# dcc.Graph(id="map-graph", 
#     #config={'displayModeBar': True}, 
#     #animate=True,
#     figure = px.scatter(df, 
#         x='x', 
#         y='y',
#         color='main_label',
#         hover_name='title', 
#         hover_data=['authors','doi','year','type','main_keys'], 
#         color_discrete_sequence=px.colors.qualitative.D3, 
#         opacity=0.6, 
#         template='plotly_white').update_layout(
#            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#             'paper_bgcolor': 'rgba(0, 0, 0, 0)', 
#             'xaxis_showgrid': False, 
#             'yaxis_showgrid': False, 
#             'xaxis_zeroline': False, 
#             'yaxis_zeroline': False, 
#             'yaxis_visible': False, 
#             'xaxis_visible': False, 
#             'font':{'family':"sans-serif", 'size':14, 'color':'white'},
#             'legend': {'title':'Main Topic','itemsizing': 'constant'}, 
#             'legend_font': {'family':"sans-serif", 'size':14, 'color':'white'},
#             }
#             )),

# px.scatter(df, 
#     x='x', 
#     y='y',
#     color='main_label', 
#     hover_name='title', 
#     hover_data=['authors','doi','year','type','main_keys'], 
#     color_discrete_sequence=px.colors.qualitative.D3, 
#     opacity=0.1,
#     template='plotly_white').update_layout(
#        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#         'paper_bgcolor': 'rgba(1, 1, 1, 1)', 
#         'xaxis_showgrid': False, 
#         'yaxis_showgrid': False, 
#         'xaxis_zeroline': False, 
#         'yaxis_zeroline': False, 
#         'yaxis_visible': False, 
#         'xaxis_visible': False})

# def generate_plot():
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=df['x'], y=df['y'], name='documents', mode='markers')
#         return fig

# @app.callback(
#     Output('graphs','figure'),
#     [Input('pi-selector', 'value')])

# def update_figure(selected_pi):
#     if not selected_pi:
#         fig = px.scatter(df, 
#                     x='x', 
#                     y='y',
#                     color='main_label',
#                     hover_name='title', 
#                     hover_data=['authors','doi','year','type','main_keys'], 
#                     color_discrete_sequence=px.colors.qualitative.D3, 
#                     opacity=0.6, 
#                     template='plotly_white').update_layout(
#                        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#                         'paper_bgcolor': 'rgba(0, 0, 0, 0)', 
#                         'xaxis_showgrid': False, 
#                         'yaxis_showgrid': False, 
#                         'xaxis_zeroline': False, 
#                         'yaxis_zeroline': False, 
#                         'yaxis_visible': False, 
#                         'xaxis_visible': False, 
#                         'font':{'family':"sans-serif", 'size':14, 'color':'white'},
#                         'legend': {'title':'Main Topic','itemsizing': 'constant'}, 
#                         'legend_font': {'family':"sans-serif", 'size':14, 'color':'white'},
#                         }
#                         )
#         return fig
    
#     else:
#         filtered_df = df[df.Name == selected_pi]
#         traces = []
#         for i in filtered_df.main_label.unique():
#             df_by_topic = filtered_df[filtered_df['main_label'] == i]
#             traces.append(dict(
#                 x=df_by_topic['x'],
#                 y=df_by_topic['y'],
#                 text=df_by_topic['title'],
#                 color=df_by_topic['main_label'], 
#                 # hover_name='title', 
#                 # hover_data=['authors','doi','year','type','main_keys'], 
#                 color_discrete_sequence=px.colors.qualitative.D3,
#                 mode='markers',
#                 opacity=0.7,
#                 marker={
#                     'size': 10,
#                     'line': {'width': 0, 'color': 'white'}
#                 },
#                 name=i
#             ))

#         return {
#             'data': traces,
#             'layout': dict(
#                 xaxis={'range':[-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
#                 yaxis={'range': [-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
#                 # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#                 # xaxis_showgrid=False, 
#                 # yaxis_showgrid=False, 
#                 # xaxis_zeroline=False, 
#                 # yaxis_zeroline=False, 
#                 # yaxis_visible=False, 
#                 # xaxis_visible=False,
#                 # legend={'x': 0, 'y': 1},
#                 hovermode='closest',
#                 transition = {'duration': 500},
#             )
#         }

#     return graphs

# traces = []
        # for i in filtered_df.main_label.unique():
        #     df_by_topic = filtered_df[filtered_df['main_label'] == i]
        #     traces.append(dict(
        #         x=df_by_topic['x'],
        #         y=df_by_topic['y'],
        #         text=df_by_topic['title'],
        #         color=df_by_topic['main_label'], 
        #         # hover_name='title', 
        #         # hover_data=['authors','doi','year','type','main_keys'], 
        #         color_discrete_sequence=px.colors.qualitative.D3,
        #         mode='markers',
        #         opacity=0.7,
        #         marker={
        #             'size': 10,
        #             'line': {'width': 0, 'color': 'white'}
        #         },
        #         name=i
        #     ))

        # return {
        #     'data': traces,
        #     'layout': dict(
        #         xaxis={'range':[-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
        #         yaxis={'range': [-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
        #         # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        #         # xaxis_showgrid=False, 
        #         # yaxis_showgrid=False, 
        #         # xaxis_zeroline=False, 
        #         # yaxis_zeroline=False, 
        #         # yaxis_visible=False, 
        #         # xaxis_visible=False,
        #         # legend={'x': 0, 'y': 1},
        #         hovermode='closest',
        #         transition = {'duration': 500},
        #     )
        # }

# @app.callback(
#     Output('map-graph', 'figure'),
#     [Input('pi-selector', 'value')])

# def update_figure(selected_pi):
#     filtered_df = df[df.Name == selected_pi]
#     traces = []
#     for i in filtered_df.main_label.unique():
#         df_by_topic = filtered_df[filtered_df['main_label'] == i]
#         traces.append(dict(
#             x=df_by_topic['x'],
#             y=df_by_topic['y'],
#             text=df_by_topic['title'],
#             color=df_by_topic['main_label'], 
#             # hover_name='title', 
#             # hover_data=['authors','doi','year','type','main_keys'], 
#             color_discrete_sequence=px.colors.qualitative.D3,
#             mode='markers',
#             opacity=0.7,
#             marker={
#                 'size': 10,
#                 'line': {'width': 0, 'color': 'white'}
#             },
#             name=i
#         ))

#     return {
#         'data': traces,
#         'layout': dict(
#             xaxis={'range':[-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
#             yaxis={'range': [-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
#             # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#             # xaxis_showgrid=False, 
#             # yaxis_showgrid=False, 
#             # xaxis_zeroline=False, 
#             # yaxis_zeroline=False, 
#             # yaxis_visible=False, 
#             # xaxis_visible=False,
#             # legend={'x': 0, 'y': 1},
#             hovermode='closest',
#             transition = {'duration': 500},
#         )
#     }

# @app.callback(
#     Output('map-graph', 'figure'),
#     [Input('year-selector', 'value')])

# def update_figure(selected_yrs):

#     traces = []
#     for i in filtered_df.main_label.unique():
#         df_by_topic = filtered_df[filtered_df['main_label'] == i]
#         traces.append(dict(
#             x=df_by_topic['x'],
#             y=df_by_topic['y'],
#             text=df_by_topic['title'],
#             color=df_by_topic['main_label'], 
#             # hover_name='title', 
#             # hover_data=['authors','doi','year','type','main_keys'], 
#             color_discrete_sequence=px.colors.qualitative.D3,
#             mode='markers',
#             opacity=0.7,
#             marker={
#                 'size': 10,
#                 'line': {'width': 0, 'color': 'white'}
#             },
#             name=i
#         ))

#     return {
#         'data': traces,
#         'layout': dict(
#             xaxis={'range':[-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
#             yaxis={'range': [-150, 150],'showgrid': False,'zeroline': False,'visible': False,},
#             # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#             # xaxis_showgrid=False, 
#             # yaxis_showgrid=False, 
#             # xaxis_zeroline=False, 
#             # yaxis_zeroline=False, 
#             # yaxis_visible=False, 
#             # xaxis_visible=False,
#             # legend={'x': 0, 'y': 1},
#             hovermode='closest',
#             transition = {'duration': 500},
#         )
#     }