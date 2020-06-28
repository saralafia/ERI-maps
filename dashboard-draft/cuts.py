# app.title='ERI Research Dashboard'
# list_of_pis = df['Name'].unique().tolist()
# list_of_pis.sort()

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

# dcc.Slider(id='year-slider',
#     min=df['year'].min(),
#     max=df['year'].max(),
#     value=df['year'].max(),
#     marks={str(year): str(year) for year in df['year'].unique()}, 
#     step=None
#     ),

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


# html.Div(
#     className='eight columns div-for-charts bg-grey', 
#     children=[
#         dcc.Graph(id='change', 
#             config={'displayModeBar': False}, 
#             animate=True)])

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

# if not selected_pi:
#     fig = px.scatter(dff, 
#                 x='x', 
#                 y='y',
#                 color='main_label',
#                 hover_name='title', 
#                 hover_data=['authors','doi','year','type','main_keys'], 
#                 color_discrete_sequence=px.colors.qualitative.D3, 
#                 opacity=0.6,
#                 )

#     fig.update_layout(
#                    {'autosize': True, 
#                    'width':900,
#                    'height':700,
#                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#                     'paper_bgcolor': 'rgba(0, 0, 0, 0)', 
#                     'xaxis_showgrid': False, 
#                     'yaxis_showgrid': False, 
#                     'xaxis_zeroline': False, 
#                     'yaxis_zeroline': False, 
#                     'yaxis_visible': False, 
#                     'xaxis_visible': False, 
#                     'font':{'family':"sans-serif", 'size':14, 'color':'white'},
#                     'legend': {'title':'Main Topic','itemsizing': 'constant'}, 
#                     'legend_font': {'family':"sans-serif", 'size':14, 'color':'white'},
#                     }
#                     )

#     return fig

# elif not selected_dept:
#     fig = px.scatter(dff, 
#                 x='x', 
#                 y='y',
#                 color='main_label',
#                 hover_name='title', 
#                 hover_data=['authors','doi','year','type','main_keys'], 
#                 color_discrete_sequence=px.colors.qualitative.D3, 
#                 opacity=0.6,
#                 )

#     fig.update_layout(
#                    {'autosize': True, 
#                    'width':900,
#                    'height':700,
#                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#                     'paper_bgcolor': 'rgba(0, 0, 0, 0)', 
#                     'xaxis_showgrid': False, 
#                     'yaxis_showgrid': False, 
#                     'xaxis_zeroline': False, 
#                     'yaxis_zeroline': False, 
#                     'yaxis_visible': False, 
#                     'xaxis_visible': False, 
#                     'font':{'family':"sans-serif", 'size':14, 'color':'white'},
#                     'legend': {'title':'Main Topic','itemsizing': 'constant'}, 
#                     'legend_font': {'family':"sans-serif", 'size':14, 'color':'white'},
#                     }
#                     )

#     return fig

#else:

app.layout = html.Div(children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="four columns div-user-controls",
                    children=[
                        html.Img(className="logo", src=app.get_asset_url("ERI_logo_WEB_72dpi_1.png")),
                        html.H2("ERI Research Map"),
                        html.P(
                            """Highlight documents by an ERI researcher or from an academic department/unit."""
                        ),
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        dcc.Dropdown(id="pi-selector",
                                            placeholder="Select an ERI researcher", 
                                            options=[{"label": i, "value": i} for i in list_of_pis],
                                            multi=False,
                                            className='pi-selector',
                                            ),
                                    ]
                                ), 
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        dcc.Dropdown(id="dept-selector",
                                            placeholder="Select an academic department", 
                                            options=[{"label": i, "value": i} for i in list_of_depts],
                                            multi=False,
                                            className='dept-selector',
                                            ),
                                    ]
                                ),  
                            ],
                        ),
                        dcc.Markdown(
                            children=[
                                "**About:** This t-SNE map was created from a NMF topic model of 3,770 ERI research publications and active projects from 2001 - 2019. Dashboard data and code are available on [Github](https://github.com/saralafia/ERI-dashboard)."
                            ]
                        ),
                        # dcc.Markdown("""
                        #         **Click a document in the map for more information.**
                        #         """),
                        #html.Button('Reset selection', id='button'),
                        html.Pre(id='click-data', 
                                style=styles['pre']),
                    ],
                ),
                html.Div(
                    className="eight columns div-for-charts bg-grey",
                    children=[
                        html.Div(
                            className="text-padding",
                            children=[
                                "Select the topical granularity and embedding method of the underlying model."
                            ],
                        ),
                        dcc.RadioItems(
                            id='granularity-options',
                            options=[{'label': i, 'value': i} for i in all_options.keys()],
                            value='coarse (t-SNE)',
                            labelStyle={'display': 'inline-block', 'verticalAlign': 'top', 'width': '20%'}
                            ),
                        dcc.Graph(
                            id='graphs', 
                            config={'displayModeBar': True}, 
                            responsive=True,
                            #style={"height" : '80vh', "width" : "100%"},
                            style={"height" : "75%", "width" : "100%"},
                            ),
                        html.Div(
                            className="text-padding",
                            children=[
                                "Select start and end years to subset the documents in the map."
                            ],
                        ),
                        html.Div(
                            className="div-for-slider", 
                            children=[
                                dcc.RangeSlider(
                                    id='year--slider',
                                    min=coarse['year'].min(),
                                    max=coarse['year'].max(),
                                    value=[2009, 2019],
                                    allowCross=False,marks={str(year): str(year) for year in coarse['year'].unique()}, 
                                    step=None, 
                                    className='year--slider',
                                    ),
                                ]
                            ),
                    ]
                )
            ]
        )
    ])