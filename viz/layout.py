from dash import dcc, html
import dash_bootstrap_components as dbc


def create_slider(id, min, max, value, mark_values, step, class_name):
    marks = {i: str(year) for i, year in enumerate(mark_values)}
    return dcc.Slider(
        id=id,
        min=min,
        max=max,
        value=value,
        marks=marks,
        step=step,
        className=class_name
    )


def create_graph(id):
    return dcc.Graph(id=id)


def create_dropdown(id, options, value, multi):
    return dcc.Dropdown(
        id=id,
        options=[{'label': option, 'value': option} for option in options],
        value=value,
        multi=multi
    )


def create_container(children, className=''):
    return dbc.Container(children, className=className, fluid=True)


def create_row(children, class_name=''):
    return dbc.Row(children, className=class_name)


def create_col(children, width, class_name='', align='center'):
    return dbc.Col(children, className=class_name, width=width, align=align)


def create_app_layout(app, countries, included_years):
    return dbc.Container(
        style={'font-family': 'Arial, sans-serif', 'padding': '30px'},
        fluid=True,
        children=[
            create_row([
                create_col([
                    html.H2('World Vaccination Coverage Dashboard',
                            style={'text-align': 'center'}),
                    html.H4(
                        'Visualizing Global Vaccination Coverage from 1990 to 2020',
                        style={'text-align': 'center'}
                    ),
                    html.P(
                        'Explore vaccination coverage trends across the world from 1990 to 2020.'),
                    create_container([
                        create_slider(id='year-slider', min=0,
                                      max=len(included_years) - 1, value=0,
                                      mark_values=included_years, step=1,
                                      class_name='slider')
                    ]),
                    create_row([
                        create_col([
                            html.H3(
                                id='title',
                                style={
                                    'text-align': 'center',
                                    'margin-top': '10px',
                                    'color': 'black'
                                }
                            ),
                            create_graph('choropleth-graph')
                        ], width=8),
                        create_col(html.Div(id='vaccination-table'), width=4)
                    ]),
                    create_row([
                        create_col([
                            html.H4("Line Chart"),
                            create_dropdown(
                                'country-dropdown-line', countries, ['Germany', 'United States', 'China'], True),
                            create_graph('line-chart')
                        ], width=9),
                        create_col([
                            html.H4("Bar Chart"),
                            create_dropdown(
                                'country-dropdown-bar', countries, ['Germany', 'United States', 'China'], True),
                            create_dropdown(
                                'year-dropdown-bar', [str(year) for year in included_years], str(included_years[-1]), False),
                            create_graph('bar-chart')
                        ], width=9)
                    ]),
                    html.P("Developed By: Your Name"),
                    html.P("Data Source: Our World in Data "),
                    html.A(
                        "Source Link", href="https://ourworldindata.org/grapher/gdp-per-capita-worldbank", target="_blank")
                ], width=12)
            ])
        ]
    )
