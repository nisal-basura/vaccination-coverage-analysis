from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go


def update_title(year_index, included_years):
    year = included_years[year_index]
    return f'Vaccination Coverage {year}'


def generate_choropleth_figure(data, year):
    fig = px.choropleth(
        data_frame=data,
        locations='Code',
        locationmode='ISO-3',
        color=str(year),
        hover_data={'Country': True, str(year): ':.0f'},
        color_continuous_scale='viridis'
    )
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    return fig


def generate_table(data, year):
    data_year = data[['Country', str(year)]]
    data_year.sort_values(str(year), ascending=False, inplace=True)
    data_year['Rank'] = range(1, len(data_year) + 1)
    return data_year.head(10).to_dict('records')


def generate_line_chart(data, countries):
    filtered_data = data[data['Country'].isin(countries)]
    filtered_data = filtered_data.melt(
        id_vars=['Country'], var_name='Year', value_name='Vaccination Coverage')
    fig = px.line(
        data_frame=filtered_data,
        x='Year',
        y='Vaccination Coverage',
        color='Country'
    )
    return fig


def generate_bar_chart(data, countries, year):
    fig = px.bar(
        data_frame=data[data['Country'].isin(countries)],
        x='Country',
        y=str(year),
        orientation='h'
    )
    return fig


def generate_growth_rate_chart(data, countries):
    fig = go.Figure()
    for country in countries:
        country_data = data[data['Country'] == country]
        fig.add_trace(go.Scatter(
            x=country_data['Year'], y=country_data['Growth Rate'], mode='lines+markers', name=country))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    return fig


def register_callbacks(app, data, included_years):
    @app.callback(
        Output('title', 'children'),
        [Input('year-slider', 'value')]
    )
    def update_title_callback(year_index):
        return update_title(year_index, included_years)

    @app.callback(
        Output('choropleth-graph', 'figure'),
        [Input('year-slider', 'value')]
    )
    def update_choropleth_callback(year_index):
        year = included_years[year_index]
        return generate_choropleth_figure(data, year)

    @app.callback(
        Output('vaccination-table', 'children'),
        [Input('year-slider', 'value')]
    )
    def update_table_callback(year_index):
        year = included_years[year_index]
        return generate_table(data, year)

    @app.callback(
        Output('line-chart', 'figure'),
        [Input('country-dropdown-line', 'value')]
    )
    def update_line_chart_callback(selected_countries):
        return generate_line_chart(data, selected_countries)

    @app.callback(
        Output('bar-chart', 'figure'),
        [Input('country-dropdown-bar', 'value'),
         Input('year-dropdown-bar', 'value')]
    )
    def update_bar_chart_callback(selected_countries, selected_year):
        return generate_bar_chart(data, selected_countries, selected_year)

    # @app.callback(
    #     Output('growth-rate', 'figure'),
    #     [Input('country-dropdown-growth', 'value')]
    # )
    # def update_growth_rate_chart_callback(selected_countries):
    #     return generate_growth_rate_chart(data, selected_countries)
