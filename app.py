import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==========================================
# 1. ESTÉTICA E DESIGN & CONFIGURAÇÃO INICIAL
# ==========================================
st.set_page_config(
    page_title="EcoCloud Analytics",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. ENGENHARIA DE DADOS (Simulação)
# ==========================================
@st.cache_data
def gerar_dados_simulados():
    """
    Gera um DataFrame simulado com dados de infraestrutura Cloud.
    Período: Jan 2026 a Maio 2026.
    """
    # Fixando seed para reprodutibilidade
    np.random.seed(42)
    
    # Criando o range de datas com granularidade diária (151 dias)
    datas = pd.date_range(start="2026-01-01", end="2026-05-31", freq="D")
    
    departamentos = ["E-commerce", "BI & Analytics", "Core API", "Marketing"]
    regioes = ["us-east-1", "sa-east-1", "eu-west-1"]
    
    dados = []
    
    for data in datas:
        for depto in departamentos:
            for regiao in regioes:
                # Simulando métricas de infraestrutura
                uso_cpu = np.random.uniform(5, 100)
                custo_usd = np.random.uniform(50, 500)
                
                # Definindo fator de emissão com base na região da AWS
                # A região sa-east-1 (Brasil) possui matriz energética com fontes renováveis mais fortes
                if regiao == "sa-east-1":
                    fator_emissao = 0.4
                elif regiao == "eu-west-1":
                    fator_emissao = 0.6
                else: # us-east-1
                    fator_emissao = 1.0
                
                # Cálculo base de CO2 (em kg)
                co2_kg = custo_usd * fator_emissao * 0.8
                
                # Regras de Negócio ESG:
                # Flag de Ociosidade: CPU < 20% representa desperdício
                ocioso = 1 if uso_cpu < 20 else 0
                
                # Penalidade de CO2: recursos ociosos desperdiçam energia e emitem
                # carbono sem gerar valor de negócio tangível.
                if ocioso == 1:
                    co2_kg = co2_kg * 1.5 

                # Simulando PUE baseado na região
                if regiao == "sa-east-1":
                    pue = 1.25 + np.random.uniform(-0.05, 0.05)
                elif regiao == "eu-west-1":
                    pue = 1.15 + np.random.uniform(-0.05, 0.05)
                else: # us-east-1
                    pue = 1.30 + np.random.uniform(-0.05, 0.05)
                
                dados.append([data, depto, regiao, uso_cpu, custo_usd, co2_kg, ocioso, pue])
                
    df = pd.DataFrame(dados, columns=[
        "Data", "Departamento", "Região AWS", "Uso_CPU", "Custo_USD", "CO2_kg", "Ocioso", "PUE"
    ])
    
    return df

df_cloud = gerar_dados_simulados()

# ==========================================
# 3. ESTRUTURA DA INTERFACE & SIDEBAR
# ==========================================
st.sidebar.markdown("## ⚙️ Filtros")
st.sidebar.markdown("Selecione os parâmetros para análise:")

# Filtros com valores padrão sendo "Todos"
filtro_depto = st.sidebar.multiselect(
    "Departamento",
    options=df_cloud["Departamento"].unique(),
    default=df_cloud["Departamento"].unique()
)

filtro_regiao = st.sidebar.multiselect(
    "Região AWS",
    options=df_cloud["Região AWS"].unique(),
    default=df_cloud["Região AWS"].unique()
)

# Aplicando os filtros de forma dinâmica no DataFrame
df_filtrado = df_cloud[
    (df_cloud["Departamento"].isin(filtro_depto)) & 
    (df_cloud["Região AWS"].isin(filtro_regiao))
]

# Topo da Página Elegante
st.title("🌿 EcoCloud Analytics")
st.markdown(
    """
    <p style='color: #a0aab5; font-size: 1.1rem;'>
        Monitoramento inteligente de pegada de carbono e eficiência energética para infraestruturas Cloud.
    </p>
    """, 
    unsafe_allow_html=True
)
st.markdown("---")

# ==========================================
# 4. KPIs (Key Performance Indicators)
# ==========================================
# Cálculos
total_co2_kg = df_filtrado["CO2_kg"].sum()
total_co2_ton = total_co2_kg / 1000

# Uma árvore madura absorve aproximadamente 22kg de CO2 por ano
arvores_necessarias = int(total_co2_kg / 22)

# Custo somado apenas das máquinas subutilizadas
custo_desperdicio = df_filtrado[df_filtrado["Ocioso"] == 1]["Custo_USD"].sum()

# PUE Médio
pue_medio = df_filtrado["PUE"].mean()

# Exibição
col1, col2, col3, col4 = st.columns(4)
cor_verde = "#2ecc71" # Cor minimalista/soft de destaque

with col1:
    st.markdown(f"### Pegada de Carbono")
    st.markdown(f"<h2 style='color: {cor_verde};'>{total_co2_ton:,.2f} tCO₂</h2>", unsafe_allow_html=True)
    st.caption("Emissão total em Toneladas no período filtrado")

with col2:
    st.markdown(f"### Compensação Estimada")
    st.markdown(f"<h2 style='color: {cor_verde};'>🌳 {arvores_necessarias:,}</h2>", unsafe_allow_html=True)
    st.caption("Árvores necessárias para neutralização")

with col3:
    st.markdown(f"### Desperdício Financeiro")
    st.markdown(f"<h2 style='color: #e74c3c;'>${custo_desperdicio:,.2f}</h2>", unsafe_allow_html=True)
    st.caption("Custo USD de recursos ociosos")

with col4:
    st.markdown(f"### PUE Médio")
    st.markdown(f"<h2 style='color: #f39c12;'>{pue_medio:.2f}</h2>", unsafe_allow_html=True)
    st.caption("Eficácia do Uso de Energia (ideal < 1.2)")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 5. VISUALIZAÇÕES AVANÇADAS (Plotly)
# ==========================================
st.markdown("#### 📈 Análise Consolidada de Emissões e Eficiência")

# Layout com 2 colunas para os gráficos superiores
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    # Gráfico 1: Evolução temporal (Linha)
    st.markdown("**Evolução Temporal das Emissões (CO₂)**")
    df_timeline = df_filtrado.groupby("Data", as_index=False)["CO2_kg"].sum()
    
    fig_linha = px.line(
        df_timeline, 
        x="Data", 
        y="CO2_kg",
        template="plotly_dark",
        color_discrete_sequence=[cor_verde]
    )
    fig_linha.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="",
        yaxis_title="CO₂ (kg)",
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig_linha, width='stretch')

with col_graf2:
    # Gráfico 2: Boxplot (Distribuição do Uso_CPU por Departamento)
    st.markdown("**Distribuição de Uso de CPU por Departamento**")
    fig_box = px.box(
        df_filtrado,
        x="Departamento",
        y="Uso_CPU",
        color="Departamento",
        template="plotly_dark",
        points="all" # Exibe todos os pontos para expor assimetrias
    )
    fig_box.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="",
        yaxis_title="Uso de CPU (%)",
        showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig_box, width='stretch')

st.markdown("<br>", unsafe_allow_html=True)

# Layout com 2 colunas para os gráficos inferiores
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    # Gráfico 3: Mapa de Calor (Heatmap)
    st.markdown("**Concentração de CO₂: Região AWS vs Departamento**")
    df_heatmap = df_filtrado.groupby(["Região AWS", "Departamento"], as_index=False)["CO2_kg"].sum()
    df_heatmap_pivot = df_heatmap.pivot(index="Região AWS", columns="Departamento", values="CO2_kg")
    
    fig_heat = px.imshow(
        df_heatmap_pivot,
        labels=dict(x="Departamento", y="Região AWS", color="CO₂ (kg)"),
        x=df_heatmap_pivot.columns,
        y=df_heatmap_pivot.index,
        color_continuous_scale="Greens",
        template="plotly_dark",
        aspect="auto"
    )
    fig_heat.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=10, b=0)
    )
    st.plotly_chart(fig_heat, width='stretch')

with col_graf4:
    # Gráfico 4: Dispersão Facetada (Custo vs CO2 por Região)
    st.markdown("**Correlação Custo vs CO₂ (Facetado por Região AWS)**")
    fig_scatter_facet = px.scatter(
        df_filtrado,
        x="Custo_USD",
        y="CO2_kg",
        color="Departamento",
        facet_col="Região AWS",
        template="plotly_dark",
        hover_data={"Uso_CPU": ":.1f%"}
    )
    fig_scatter_facet.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=30, b=0)
    )
    # Ajustando títulos dos eixos dos subgráficos
    fig_scatter_facet.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    st.plotly_chart(fig_scatter_facet, width='stretch')
