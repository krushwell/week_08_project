import dash
# we are adding one more component to be able to add the graphs/tables
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# define, name and choose a theme for the app
app = dash.Dash('w08_project_dashboarding',
                external_stylesheets=[dbc.themes.VAPOR])
server = app.server

# adding a table
# redefine dublin data because it didn't have calculated columns for weekly and monthly averages
df_dublin = df_combi[df_combi["city"] == "Dublin"]
df_dublin_deduped = df_dublin[selected_columns].drop_duplicates()
df_dublin_deduped = df_dublin_deduped.sort_values(by='month', ascending=True)

# list of columns to include from data
selected_columns = ['month', 'avg_temp_month']
dublin_table = dash_table.DataTable(
    df_dublin_deduped[selected_columns].to_dict('records'),
    columns=[{"name": col, "id": col} for col in selected_columns],
)

# cities line graph
cities_line_plot = px.line(df_cities_visited, x='month', y='avg_temp_month',
                           height=300, title="Average Temperature by Month")
cities_line_plot.show()
graph2 = dcc.Graph(figure=cities_line_plot)

# adding the main and secondary headers with styling
app.layout = html.Div([html.H1('Temperature Analysis of Dublin', style={'textAlign': 'center'}),
                       html.H2('Dublin\'s Temperature vs Other Cities Katie Traveled in 2023', style={
                               'textAlign': 'center'}),
                       html.H3('Dublin:', style={'textAlign': 'center'}),
                       html.Div(dublin_table),
                       ])

if __name__ == '__main__':
    app.run_server(port=8084)
