# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

#Incorporate data
ibge_df = pd.read_json('https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome')

# Transforming data

## Extracting regions and abbreviations

ibge_df['regiao_nome'] = ibge_df['regiao'].apply(lambda x: x['nome'])
ibge_df['regiao_sigla'] = ibge_df['regiao'].apply(lambda x: x['sigla'])

## Add Regions Colors

regions_colors = {
    'Norte': '#1f77b4',       
    'Nordeste': '#ff7f0e',    
    'Centro-Oeste': '#2ca02c',
    'Sudeste': '#d62728',     
    'Sul': '#9467bd'          
}

ibge_df['region_color'] = ibge_df['regiao_nome'].map(regions_colors)

## Add States Colors

states_colors = {
    'AC': '#1f77b4', 'AL': '#ff7f0e', 'AP': '#2ca02c', 'AM': '#d62728',
    'BA': '#9467bd', 'CE': '#8c564b', 'DF': '#e377c2', 'ES': '#7f7f7f',
    'GO': '#bcbd22', 'MA': '#17becf', 'MT': '#aec7e8', 'MS': '#ffbb78',
    'MG': '#98df8a', 'PA': '#ff9896', 'PB': '#c5b0d5', 'PR': '#c49c94',
    'PE': '#f7b6d2', 'PI': '#c7c7c7', 'RJ': '#dbdb8d', 'RN': '#9edae5',
    'RS': '#393b79', 'RO': '#637939', 'RR': '#8c6d31', 'SC': '#843c39',
    'SP': '#7b4173', 'SE': '#3182bd', 'TO': '#fdd0a2'
}

ibge_df['state_color'] = ibge_df['sigla'].map(states_colors)

## Selecting columns
ibge_df = ibge_df[['id', 'sigla', 'nome', 'state_color', 'regiao_nome', 'region_color', 'regiao_sigla']]
ibge_df.columns = ['cod_ibge', 'UF', 'state', 'state_color', 'region', 'region_color', 'short_region'] # rename columns

# Initialize the app

app = Dash(__name__)

# App Layout

app.layout = html.Div([
    html.Div([
        html.Header("Color Map", className="title"),
        dcc.RadioItems(
            options=[
                {'label':'Per Region','value':'region'},
                {'label':'Per State','value':'state'},
            ],
            value='region',
            id='control-macro',
            className="radio-header"
        )
    ], className="header"),
    html.Div([
        html.Label(id='dropdown-title-macro',className="title-filter-sidebar"),
        dcc.Dropdown(
            id='control-region-state',
            multi=True,
            className="filter-sidebar"
        )
    ],className="sidebar"),
    html.Div([
        dcc.Graph(
            id="map-colored",
            style={"height": "85vh", "width": "100%"},
            className="visualization"
        )
    ],className="main")
], className="dashboard")

@app.callback(
    Output('control-region-state', 'options'),
    Output('control-region-state', 'value'),
    Input('control-macro', 'value')
)
def refresh_dropdown(type):
    options = [{'label': v, 'value': v} for v in sorted(ibge_df[type].unique())]
    return options, []  # seleção default

@app.callback(
    Output('map-colored', 'figure'),
    Output('dropdown-title-macro', 'children'),
    Input('control-macro', 'value'),
    Input('control-region-state', 'value')
)
def update_map(type, selection):
    if not isinstance(selection, list):
        selection = [selection]

    label_col = 'region' if type == 'region' else 'state'
    color_col = 'region_color' if type == 'region' else 'state_color'

    df_map = ibge_df.copy()
    df_map['plot_label'] = df_map.apply(
        lambda row: row[label_col] if row[label_col] in selection else 'Out of Range',
        axis=1
    )

    # Mapa de cores (nome → cor), adicionando branco para os que não estão selecionados
    color_discrete_map = {
        row[label_col]: row[color_col]
        for _, row in ibge_df.iterrows()
    }
    color_discrete_map['Out of Range'] = '#FFFFFF'

    fig = px.choropleth(
        df_map,
        geojson='https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson',
        locations='cod_ibge',
        featureidkey='properties.codigo_ibg',
        color='plot_label',
        scope="south america",
        color_discrete_map=color_discrete_map,
        labels={'plot_label': "Regions" if type == "region" else "States"}
    )

    fig.update_geos(
        visible=True,
        scope="south america",
        projection_type="mercator",
        projection_scale=1.5,
        center={"lat": -14.2350, "lon": -51.9253},
        showland=True,
        landcolor="light gray",
    )

    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        legend=dict(font=dict(color="black")),
        legend_title_text="Regions" if type == "region" else "States"
    )

    title="Region:" if type == 'region' else "State:"

    return fig, title

# Run the app
if __name__ == '__main__':
    app.run(debug=True)