import streamlit as st
import pandas as pd
import plotly.express as px

# ====== Configuração Geral ======
st.set_page_config(page_title="Dashboard Consolidado", layout="wide")

# ====== Dados ======
data_programas = {
    "Programa": ["Acredita no Primeiro Passo", "Procred 360", "Resumo Consolidado"],
    "Operações": [47895, 41766, 89661],
    "Valor Total (R$)": [431746250.00, 1205303.22, 433951553.22]
}
df_programas = pd.DataFrame(data_programas)

data_detalhamento = {
    "Instituição": [
        "Banco do Nordeste (BNB)", "Agência de Fomento do Piauí (Badespi)", 
        "Banco da Amazônia", "Agência de Fomento do RN", "Banco do Estado do Pará",
        "Banco do Brasil", "Caixa Econômica Federal"
    ],
    "Programa": [
        "Acredita no Primeiro Passo", "Acredita no Primeiro Passo", "Acredita no Primeiro Passo",
        "Acredita no Primeiro Passo", "Acredita no Primeiro Passo", 
        "Procred 360", "Procred 360"
    ],
    "Operações": [47603, 100, 119, 68, 5, 27288, 14488],
    "Valor Total (R$)": [
        430213958.16, 517380.40, 465512.00, 531900.00, 17500.00,
        787303383.82, 417999938.96
    ]
}
df_detalhamento = pd.DataFrame(data_detalhamento)

data_bancos = {
    "Banco": ["BNB", "BNB", "BNB", "BNB", "BNB", "BNB", "BNB", "BNB", "BNB", "BNB", "BNB", "BADESPI", "BASA", "BASA", "AFRN", "BANPARÁ"],
    "UF": ["AL", "BA", "CE", "ES", "MA", "MG", "PB", "PE", "PI", "RN", "SE", "PI", "PA", "PA", "RN", "PA"],
    "Total de Operações": [1387, 5574, 12083, 235, 1558, 5266, 5373, 5224, 3566, 4334, 3003, 100, 119, 5, 68, 5],
    "Valor Total (R$)": [
        13782585.71, 51967988.17, 93520973.75, 2336412.84, 12627464.81,
        53397435.34, 55310909.26, 45885081.02, 35095594.38, 40657593.38,
        25901919.50, 517380.47, 465512.00, 17500.00, 531900.00, 17500.00
    ]
}
df_bancos = pd.DataFrame(data_bancos)

data_procred = {
    "UF": ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"],
    "Total de Operações": [78, 377, 242, 67, 2138, 946, 342, 446, 1120, 543, 3410, 451, 401, 539, 598, 810, 373, 2083, 1576, 351, 311, 61, 1570, 1230, 396, 6615, 314],
    "Valor Total (R$)": [
        2180482.70, 11385108.60, 5792046.05, 2986007.11, 58812644.73, 
        27689741.49, 10657201.73, 12467035.59, 31093647.09, 17707440.96, 
        94403483.33, 13010971.25, 11534941.60, 15788336.34, 16787676.11, 
        24169098.89, 10693652.22, 58103612.18, 45213227.54, 10266311.04, 
        6273118.21, 1977861.74, 44225128.31, 36108953.47, 12810463.35, 
        196848453.70, 8316738.49
    ]
}
df_procred = pd.DataFrame(data_procred)

# ====== Layout ======
st.title("Dashboard Consolidado")

# Tabs de seleção
tab = st.radio("Selecione a visualização:", ["Programas de Crédito", "Acredita no Primeiro Passo", "PROCRED 360"])

# ====== Conteúdo das Abas ======
if tab == "Programas de Crédito":
    st.header("Programas de Crédito")
    programa_select = st.selectbox("Selecione um programa", ["Todos"] + list(df_programas["Programa"].unique()))

    if programa_select == "Todos":
        df_programas_filtered = df_programas
        df_detalhamento_filtered = df_detalhamento
    else:
        df_programas_filtered = df_programas[df_programas["Programa"] == programa_select]
        df_detalhamento_filtered = df_detalhamento[df_detalhamento["Programa"] == programa_select]

    st.subheader(f"Resultados para: {programa_select}")
    st.write(df_programas_filtered)
    st.write(df_detalhamento_filtered)

    # Gráficos de barra
    st.plotly_chart(px.bar(df_programas_filtered, x="Programa", y="Operações", title="Operações por Programa", text="Operações"))
    st.plotly_chart(px.bar(df_programas_filtered, x="Programa", y="Valor Total (R$)", title="Valores Totais por Programa", text="Valor Total (R$)"))
    st.plotly_chart(px.bar(df_detalhamento_filtered, x="Instituição", y="Operações", title="Operações por Instituição", text="Operações"))
    st.plotly_chart(px.bar(df_detalhamento_filtered, x="Instituição", y="Valor Total (R$)", title="Valores Totais por Instituição", text="Valor Total (R$)"))
    st.plotly_chart(px.bar(df_detalhamento_filtered, x="Programa", y="Operações", title="Operações Consolidadas por Programa", text="Operações"))

    # Gráficos de pizza
    st.plotly_chart(px.pie(df_programas_filtered, names="Programa", values="Operações", title="Proporção de Operações por Programa"))
    st.plotly_chart(px.pie(df_programas_filtered, names="Programa", values="Valor Total (R$)", title="Proporção de Valores Totais por Programa"))

elif tab == "Acredita no Primeiro Passo":
    st.header("Acredita no Primeiro Passo")
    ufs_select = st.multiselect("Selecione os estados", ["Todos"] + list(df_bancos["UF"].unique()), default=["Todos"])

    if "Todos" in ufs_select:
        df_bancos_filtered = df_bancos
    else:
        df_bancos_filtered = df_bancos[df_bancos["UF"].isin(ufs_select)]

    st.subheader(f"Resultados para: {', '.join(ufs_select)}")
    st.write(df_bancos_filtered)

    # Gráficos de barra
    st.plotly_chart(px.bar(df_bancos_filtered, x="UF", y="Total de Operações", title="Total de Operações por Estado"))
    st.plotly_chart(px.bar(df_bancos_filtered, x="UF", y="Valor Total (R$)", title="Valores Totais por Estado"))
    st.plotly_chart(px.bar(df_bancos_filtered, x="Banco", y="Total de Operações", title="Operações por Banco"))
    st.plotly_chart(px.bar(df_bancos_filtered, x="Banco", y="Valor Total (R$)", title="Valor Total por Banco"))
    st.plotly_chart(px.bar(df_bancos_filtered, x="UF", y="Total de Operações", title="Distribuição de Operações por Estado"))

    # Gráficos de pizza
    st.plotly_chart(px.pie(df_bancos_filtered, names="UF", values="Total de Operações", title="Proporção de Operações por Estado"))
    st.plotly_chart(px.pie(df_bancos_filtered, names="UF", values="Valor Total (R$)", title="Proporção de Valores Totais por Estado"))

elif tab == "PROCRED 360":
    st.header("PROCRED 360")
    ufs_select = st.multiselect("Selecione os estados", ["Todos"] + list(df_procred["UF"].unique()), default=["Todos"])

    if "Todos" in ufs_select:
        df_procred_filtered = df_procred
    else:
        df_procred_filtered = df_procred[df_procred["UF"].isin(ufs_select)]

    st.subheader(f"Resultados para: {', '.join(ufs_select)}")
    st.write(df_procred_filtered)

    # Gráficos de barra
    st.plotly_chart(px.bar(df_procred_filtered, x="UF", y="Total de Operações", title="Total de Operações por Estado"))
    st.plotly_chart(px.bar(df_procred_filtered, x="UF", y="Valor Total (R$)", title="Valores Totais por Estado"))
    st.plotly_chart(px.bar(df_procred_filtered, x="UF", y="Total de Operações", title="Distribuição de Operações por UF"))
    st.plotly_chart(px.bar(df_procred_filtered, x="UF", y="Valor Total (R$)", title="Distribuição de Valores Totais por UF"))
    st.plotly_chart(px.bar(df_procred_filtered, x="UF", y=df_procred_filtered["Valor Total (R$)"] / df_procred_filtered["Total de Operações"], title="Valores Médios por UF"))

    # Gráficos de pizza
    st.plotly_chart(px.pie(df_procred_filtered, names="UF", values="Total de Operações", title="Proporção de Operações por Estado"))
    st.plotly_chart(px.pie(df_procred_filtered, names="UF", values="Valor Total (R$)", title="Proporção de Valores Totais por Estado"))
