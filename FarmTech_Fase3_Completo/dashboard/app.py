import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FarmTech Solutions - Dashboard", layout="wide")

st.title("FarmTech Solutions - Dashboard de Sensores")
st.write("Visualização dos dados coletados pelos sensores agrícolas da Fase 2.")

df = pd.read_csv("../dados/dados_sensores_fase2.csv", sep=";")

cultura = st.sidebar.multiselect(
    "Filtrar cultura",
    sorted(df["cultura"].unique()),
    default=sorted(df["cultura"].unique())
)

df_filtrado = df[df["cultura"].isin(cultura)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Média Umidade", f"{df_filtrado['umidade'].mean():.2f}%")
col2.metric("Média pH", f"{df_filtrado['ph'].mean():.2f}")
col3.metric("Média Fósforo", f"{df_filtrado['fosforo_p'].mean():.2f}")
col4.metric("Média Potássio", f"{df_filtrado['potassio_k'].mean():.2f}")

st.subheader("Tabela de Dados")
st.dataframe(df_filtrado, use_container_width=True)

st.subheader("Umidade por Registro")
fig_umidade = px.line(df_filtrado, x="id", y="umidade", color="cultura", markers=True)
st.plotly_chart(fig_umidade, use_container_width=True)

st.subheader("Níveis de P, K e pH")
fig_pk = px.scatter(
    df_filtrado,
    x="fosforo_p",
    y="potassio_k",
    color="cultura",
    size="ph",
    hover_data=["umidade", "temperatura", "status_irrigacao"]
)
st.plotly_chart(fig_pk, use_container_width=True)

st.subheader("Status da Irrigação")
status = df_filtrado["status_irrigacao"].value_counts().reset_index()
status.columns = ["status_irrigacao", "total"]
fig_status = px.bar(status, x="status_irrigacao", y="total", text="total")
st.plotly_chart(fig_status, use_container_width=True)

st.subheader("Sugestão de Irrigação")
media_umidade = df_filtrado["umidade"].mean()
media_temp = df_filtrado["temperatura"].mean()

if media_umidade < 50:
    st.warning("Sugestão: manter ou iniciar irrigação, pois a umidade média está baixa.")
elif media_temp > 30:
    st.warning("Sugestão: monitorar irrigação, pois a temperatura média está alta.")
else:
    st.success("Sugestão: irrigação pode permanecer desligada no momento.")
