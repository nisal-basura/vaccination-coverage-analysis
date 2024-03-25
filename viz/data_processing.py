import pandas as pd


def load_data(file_path):
    data = pd.read_csv("C:\\Users\\HP\\Desktop\\viz\\viz\\vaccination_coverage_clean.csv")
    data = data.rename(columns={'Entity': 'Country'})
    return data


def get_unique_countries(data):
    return data['Country'].unique()


def get_included_years(start, end):
    return range(start, end)
