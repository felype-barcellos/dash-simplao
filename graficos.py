import plotly.express as px
import pandas as pd 

def grafico_linhas(x_dados, y_dados, titulo):
    df_para_plot = pd.DataFrame({'Eixo X': x_dados,'Eixo Y': y_dados})
    fig = px.line(df_para_plot, x='Eixo X', y='Eixo Y', title=titulo, markers=True)
    return fig

def grafico_barras(x_dados, y_dados, titulo):
    df_para_plot = pd.DataFrame({'Eixo X': x_dados, 'Eixo Y': y_dados})
    fig = px.bar(df_para_plot, x='Eixo X', y='Eixo Y', title=titulo)
    return fig


def grafico_pizza(x_dados, y_dados, titulo):
    df_para_plot = pd.DataFrame({'Eixo X': x_dados, 'Eixo Y': y_dados})
    fig = px.pie(df_para_plot, names='Eixo X', values='Eixo Y', title=titulo)
    return fig

def grafico_boxplot(x_dados, y_dados, titulo):
    df_para_plot = pd.DataFrame({'Eixo X': x_dados, 'Eixo Y': y_dados})
    fig = px.box(df_para_plot, x='Eixo X', y='Eixo Y', title=titulo)
    return fig

def grafico_area(x_dados, y_dados, titulo):
    df_para_plot = pd.DataFrame({'Eixo X': x_dados, 'Eixo Y': y_dados})
    fig = px.area(df_para_plot, x='Eixo X', y='Eixo Y', title=titulo)
    return fig

def grafico_scatter_geo(x_dados, y_dados, titulo):
    df_para_plot = pd.DataFrame({'Eixo X': x_dados, 'Eixo Y': y_dados})
    fig = px.scatter_geo(df_para_plot, lat='Eixo X', lon='Eixo Y', title=titulo)
    return fig