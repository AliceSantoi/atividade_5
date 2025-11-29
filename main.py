import pandas as pd
import plotly.express as px
import streamlit as st

st.title("VACINAÇÃO - um painel informativo sobre as vacinações contra covid19 - ano 2021 ")
st.set_page_config(page_title = "DASHVACINA", layout = "wide")

df = pd.read_csv('vacinacao_corrigido.csv')

df['date'] = pd.to_datetime(df['date'])

fig1 = px.line(df, x = 'date', y = 'total_vaccinations', color = 'location', title = "Total de vacinações por país:" )
fig1.update_layout(xaxis_title = "Data", yaxis_title = "Total de vacinações")
fig1.show()

df_br_eua_ind = df.query("location == 'BRAZIL' or location == 'UNITED STATES' or location == 'INDIA'")

fig2 = px.pie(df_br_eua_ind, values = 'people_fully_vaccinated', names = 'location', title = 'Pessoas totalmente vacinadas')
fig2.show()

st.plotly_chart(fig1, use_contend_width = True)
st.plotly_chart(fig2, use_contend_width = True)

