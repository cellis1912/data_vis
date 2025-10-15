import pandas as pd
import altair as alt
import panel as pn
from panel.interact import interact

pn.extension('vega')
alt.renderers.enable("browser")
imd_df = pd.read_csv('country_economics_data.csv')

def top_gdp():
    top10 = imd_df.nlargest(10, 'GDP') 
    chart = alt.Chart(top10).mark_bar().encode(
        x=alt.X('GDP:Q', title='GDP (in billions)'),
        y=alt.Y('Name:N', sort='-x', title='Country')
    ).properties(title="Top 10 GDPs")
    return chart

top_gdp()

import altair as alt
import pandas as pd
interval = alt.selection_interval()


def gdp_popu():
    chart = alt.Chart(imd_df).mark_point().encode(
        x=alt.X('GDP:Q', title='GDP (in billions)'),
        y=alt.Y('Population:Q', title='Population (millions)')).properties(
        title="GDP vs Population"
    ).add_selection(interval)
    return chart


def line_of_bf():
    base = gdp_popu()
    
    regression_line = base.transform_regression(
        'GDP', 'Population'
    ).mark_line(color='red')
    
    return base + regression_line

line_of_bf()

# Get unique region names
region_options = sorted(imd_df["Region"].unique())

# Example interactive function
def scatter_plot(region):
    filtered = imd_df[imd_df["Region"] == region]
    chart = alt.Chart(filtered).mark_bar().encode(
        x='Debt/GDP',
        y = alt.Y('Name:N', sort='-x', title='Country')
    ).properties(title=f"Countries in {region}")
    return(chart)

# Create dropdown for region
interact(scatter_plot, region=region_options)

#Set up a scatter plot displaying the IMD Rank of the different districts
alt.Chart(imd_df).mark_point().encode(
    x='Debt/GDP',
    y='Name'
).transform_filter(alt.FieldEqualPredicate(field='Region', equal='Europe'))