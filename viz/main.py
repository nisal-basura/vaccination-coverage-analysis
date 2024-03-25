import dash
import pandas as pd

from callbacks import register_callbacks
from constants import DATA_FILE_PATH, EXTERNAL_STYLESHEETS
from layout import create_app_layout

app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
data = pd.read_csv('D:\\OW\\fiveer\\Orders\\Order 4\\viz\\viz\\vaccination_coverage_clean.csv')
data = data.rename(columns={'Entity': 'Country'})
countries = data['Country'].unique()
included_years = range(1990, 2022)

app.layout = create_app_layout(app, countries, included_years)
register_callbacks(app, data, included_years)

if __name__ == '__main__':
    app.run_server(debug=True)
