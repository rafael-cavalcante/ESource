'''from django_plotly_dash import DjangoDash
from dash import dcc, html
import plotly.express as px'''
from django_plotly_dash import DjangoDash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

import os
from django.conf import settings

app = DjangoDash('Dashboard', external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=["https://cdn.plot.ly/plotly-3.0.1.min.js"])  # nome único

# Caminho absoluto para o CSV
csv_path = os.path.join(settings.BASE_DIR, 'ESource', 'source', 'Dados extraidos dos artigos.csv')

# Lendo os dados para um DataFrame
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')

# Criado cabeçalho do dataframe
df.columns = ["ID", "Título", "Ano", "Autores", "Instituições", "Estados", "Área", "Links"]

# Dividir autores em lista
df['Autores'] = df['Autores'].str.split(',')

# Dividir instituições em lista
df['Instituições'] = df['Instituições'].str.rstrip(',').str.split(',')

# Dividir estados em lista
df['Estados'] = df['Estados'].str.rstrip(',').str.split(',')

# Contar número de autores
df['Número de Autores'] = df['Autores'].apply(len)

# Pré-processamento: extrair e contar autores por instituição
# Primeiro, vamos expandir as listas de instituições e autores
df_expanded = df.explode('Instituições')

# Contar autores por instituição
inst_counts = df_expanded['Instituições'].value_counts().reset_index()
inst_counts.columns = ['Instituição', 'Quantidade de Autores']

# Pré-processamento: contar artigos por área
area_counts = df['Área'].value_counts().reset_index()
area_counts.columns = ['Área', 'Quantidade de Artigos']

# Pré-processamento: extrair e contar autores por estado
df_expanded = df.explode('Estados')
state_counts = df_expanded['Estados'].value_counts().reset_index()
state_counts.columns = ['Estado', 'Quantidade de Autores']

# Ordenar os estados por quantidade de autores
state_counts = state_counts.sort_values('Quantidade de Autores', ascending=False)

# Pré-processamento dos dados
df_expanded = df.explode('Autores').explode('Estados')
# --------------------
# LAYOUT
# --------------------
app.layout = html.Div([
    html.H1("Quantidade de Artigos por Ano", style={'textAlign': 'center'}),
    html.Div([
        dcc.RangeSlider(
            id='year-slider',
            min=df['Ano'].min(),
            max=df['Ano'].max(),
            step=1,
            value=[df['Ano'].min(), df['Ano'].max()],
            marks={str(year): str(year) for year in df['Ano'].unique()}
        )
    ], style={'width': '80%', 'margin': '0 auto', 'padding': '20px'}),

    dcc.Graph(id='articles-by-year'),

    html.H1("Quantidade de Autores por Instituição", style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='institution-dropdown',
            options=[{'label': inst, 'value': inst} for inst in inst_counts['Instituição']],
            value=inst_counts['Instituição'].head(10).tolist(),
            multi=True
        )
    ], style={'width': '80%', 'margin': '0 auto', 'padding': '20px'}),

    dcc.Graph(id='authors-by-institution'),

    html.H1("Quantidade de Artigos por Área de Pesquisa", style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='area-dropdown',
            options=[{'label': area, 'value': area} for area in area_counts['Área']],
            value=area_counts['Área'].tolist(),
            multi=True
        )
    ], style={'width': '80%', 'margin': '0 auto', 'padding': '20px'}),

    dcc.Graph(id='articles-by-area'),

    dbc.Row([dbc.Col([html.H1("Autores por Estado Brasileiro", className="text-center mt-3 mb-4")])]),
    dbc.Row([
        dbc.Col([
            html.H4("Seleção de Estados"),
            dcc.Checklist(
                id='state-checklist',
                options=[{'label': f"{state} ({count})", 'value': state}
                         for state, count in zip(state_counts['Estado'], state_counts['Quantidade de Autores'])],
                value=state_counts['Estado'].head(5).tolist(),
                labelStyle={'display': 'block'},
            )
        ], md=3, className="bg-light p-4"),
        dbc.Col([
            dcc.Graph(id='authors-by-state-chart')
        ], md=9)
    ]),

    dbc.Row([dbc.Col([html.H1("Distribuição de Artigos por Autores e Estados",
                              className="text-center mt-3 mb-4")])]),

    dbc.Row([
        dbc.Col([
            html.H4("Filtrar por Intervalo de Anos"),
            dcc.RangeSlider(
                id='year-slider2',
                min=df['Ano'].min(),
                max=df['Ano'].max(),
                step=1,
                marks={str(year): str(year) for year in df['Ano'].unique()},
                value=[df['Ano'].min(), df['Ano'].max()],
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ])
    ]),

    dbc.Row([dbc.Col([dcc.Graph(id='icicle-chart', style={'height': '800px'})])])
])

# --------------------
# CALLBACKS
# --------------------

@app.callback(
    Output('articles-by-year', 'figure'),
    Input('year-slider', 'value')
)
def update_articles_by_year(selected_years):
    filtered_df = df[(df['Ano'] >= selected_years[0]) & (df['Ano'] <= selected_years[1])]
    counts = filtered_df['Ano'].value_counts().sort_index().reset_index()
    counts.columns = ['Ano', 'Quantidade']
    fig = px.line(counts, x='Ano', y='Quantidade', markers=True)
    return fig

@app.callback(
    Output('authors-by-institution', 'figure'),
    Input('institution-dropdown', 'value')
)
def update_authors_by_institution(selected_institutions):
    filtered = inst_counts[inst_counts['Instituição'].isin(selected_institutions)]
    fig = px.bar(filtered, x='Instituição', y='Quantidade de Autores')
    return fig

@app.callback(
    Output('articles-by-area', 'figure'),
    Input('area-dropdown', 'value')
)
def update_articles_by_area(selected_areas):
    filtered = area_counts[area_counts['Área'].isin(selected_areas)]
    filtered = filtered.sort_values('Quantidade de Artigos', ascending=True)
    fig = px.bar(filtered, y='Área', x='Quantidade de Artigos', orientation='h')
    return fig

@app.callback(
    Output('authors-by-state-chart', 'figure'),
    Input('state-checklist', 'value')
)
def update_authors_by_state(selected_states):
    filtered = state_counts[state_counts['Estado'].isin(selected_states)]
    fig = px.area(filtered, x='Estado', y='Quantidade de Autores')
    return fig

@app.callback(
    Output('icicle-chart', 'figure'),
    Input('year-slider2', 'value')
)
def update_icicle_chart(year_range):
    filtered = df_expanded[(df_expanded['Ano'] >= year_range[0]) & (df_expanded['Ano'] <= year_range[1])]
    grouped = filtered.groupby(['Estados', 'Autores']).size().reset_index(name='Quantidade')
    fig = px.icicle(grouped, path=['Estados', 'Autores'], values='Quantidade')
    return fig