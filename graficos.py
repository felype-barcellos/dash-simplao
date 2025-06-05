import plotly.express as px
import pandas as pd 

def criar_grafico_simples(x_data, y_data, titulo="Meu Gráfico"):
    df_para_plot = pd.DataFrame({
        'Eixo X': x_data,
        'Eixo Y': y_data
    })
    fig = px.line(df_para_plot, x='Eixo X', y='Eixo Y', title=titulo, markers=True)
    return fig  