import streamlit as st
from graficos import criar_grafico_simples 

st.set_page_config(layout="centered") 

st.title("Dashboard Reduzido com 1 Gráfico 📊")

st.write("Este exemplo demonstra como passar dados do script principal para uma função de plotagem em outro arquivo.")

valores_x = [1, 2, 3, 4, 5, 6, 7, 8]
valores_y = [10, 12, 8, 15, 14, 17, 13, 18]
titulo_do_grafico = "Desempenho Semanal"

st.markdown("---") 
st.subheader(titulo_do_grafico)

figura_do_grafico = criar_grafico_simples(x_data=valores_x, y_data=valores_y, titulo=titulo_do_grafico)

st.plotly_chart(figura_do_grafico, use_container_width=True)

st.markdown("---")
st.write("Fim do exemplo.")