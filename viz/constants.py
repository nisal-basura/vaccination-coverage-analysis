import dash_bootstrap_components as dbc

EXTERNAL_STYLESHEETS = [dbc.themes.ZEPHYR]

COLOR_SCHEME_PRIMARY = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA',
                        '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
COLOR_SCHEME_SECONDARY = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

APP_TITLE = 'World Vaccination Coverage Dashboard'
DATA_SOURCE_URL = 'https://ourworldindata.org/vaccination'
DATA_FILE_PATH = 'vaccination_coverage_clean.csv'

DEFAULT_COUNTRIES = ['Germany', 'United States', 'China']
DEFAULT_YEAR_RANGE = (1990, 2022)

YEAR_SLIDER_STEP = 1

GLOBAL_FONT_FAMILY = 'Arial, sans-serif'
GLOBAL_TEXT_COLOR = '#212529'
