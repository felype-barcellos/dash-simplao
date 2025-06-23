import streamlit as st
from dados import ler_arquivo
import graficos as gf

st.set_page_config(page_title="Introdução a Analise de Dados Craftsmith", layout="wide")
st.title("Sou Apenas um Dashboard Simplão")

local_arquivo_acidentes =r'acidentes2025_todas_causas_tipos.csv'
datatran = ler_arquivo(local_arquivo_acidentes)

# criando grafico de linhas
eixo_x_linha = datatran.groupby('data_inversa')['id'].nunique().reset_index(name='total_acidentes')['data_inversa']
eixo_y_linha = datatran.groupby('data_inversa')['id'].nunique().reset_index(name='total_acidentes')['total_acidentes']
titulo_linha = "Analise quantidade de acidentes por dia"
meu_grafico_linha = gf.grafico_linhas(eixo_x_linha, eixo_y_linha, titulo_linha)
st.plotly_chart(meu_grafico_linha, use_container_width=True)

# criando grafico de barras
eixo_x_barras = datatran.groupby(datatran['horario'].str.slice(0, 2))['id'].nunique().reset_index(name='total_acidentes')['horario']
eixo_y_barras = datatran.groupby(datatran['horario'].str.slice(0, 2))['id'].nunique().reset_index(name='total_acidentes')['total_acidentes']
titulo_barras = "Analise quantidade de acidentes por hora"
meu_grafico_barras = gf.grafico_barras(eixo_x_barras, eixo_y_barras, titulo_barras)
st.plotly_chart(meu_grafico_barras, use_container_width=True)

# criando grafico de pizza
eixo_x_pizza = datatran.groupby('fase_dia')['id'].nunique().reset_index(name='total_acidentes')['fase_dia']
eixo_y_pizza = datatran.groupby('fase_dia')['id'].nunique().reset_index(name='total_acidentes')['total_acidentes']
titulo_pizza = "Analise quantidade de acidentes por fase do dia"
meu_grafico_pizza = gf.grafico_pizza(eixo_x_pizza, eixo_y_pizza, titulo_pizza)
#st.plotly_chart(meu_grafico_pizza, use_container_width=True)

# criando grafico de boxplot
eixo_x_boxplot = datatran.groupby('estado_fisico')['id'].nunique().reset_index(name='total_acidentes')['estado_fisico']
eixo_y_boxplot = datatran.groupby('estado_fisico')['id'].nunique().reset_index(name='total_acidentes')['total_acidentes']
titulo_boxplot = "Analise quantidade de acidentes por estado fisico"
meu_grafico_boxplot = gf.grafico_boxplot(eixo_x_boxplot, eixo_y_boxplot, titulo_boxplot)
#st.plotly_chart(meu_grafico_boxplot, use_container_width=True)

# criando grafico de area
eixo_x_area = datatran.groupby('dia_semana')['id'].nunique().reset_index(name='total_acidentes')['dia_semana']
eixo_y_area = datatran.groupby('dia_semana')['id'].nunique().reset_index(name='total_acidentes')['total_acidentes']
titulo_area = "Analise quantidade de acidentes por dia da semana"
meu_grafico_area = gf.grafico_area(eixo_x_area, eixo_y_area, titulo_area)
#st.plotly_chart(meu_grafico_area, use_container_width=True)

# Agrupando gráfico de pizza e boxplot lado a lado
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(meu_grafico_pizza, use_container_width=True)
with col2:
    st.plotly_chart(meu_grafico_boxplot, use_container_width=True)

# criando grafico de geografico
eixo_latitude = datatran[['latitude', 'longitude']].drop_duplicates()['latitude'].astype(str).str.replace(',', '.').astype(float)
eixo_longitude = datatran[['latitude', 'longitude']].drop_duplicates()['longitude'].astype(str).str.replace(',', '.').astype(float)
titulo_geo = "Analise quantidade de acidentes por localizacao"
meu_grafico_geo = gf.grafico_scatter_geo(eixo_latitude, eixo_longitude, titulo_geo)
#st.plotly_chart(meu_grafico_geo, use_container_width=True)


# Agrupando gráfico de area e geografico lado a lado
col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(meu_grafico_area, use_container_width=True)
with col4:
    st.plotly_chart(meu_grafico_geo, use_container_width=True)