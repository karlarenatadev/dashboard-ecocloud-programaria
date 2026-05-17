# 🌿 EcoCloud Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-Express-brightgreen.svg)
![PrograMaria](https://img.shields.io/badge/Feito%20com%20💜-PrograMaria-purple.svg)

**EcoCloud Analytics** é um dashboard interativo desenvolvido como parte dos meus estudos junto à comunidade/cursos da **[PrograMaria](https://www.programaria.org/)**. O projeto tem como objetivo simular e monitorar de forma inteligente a pegada de carbono, os custos e a eficiência energética de uma infraestrutura em nuvem (simulação AWS).

---

## 🎯 Objetivo do Projeto

Aplicar conceitos de engenharia e análise de dados focados em métricas **ESG (Ambiental, Social e Governança)**, demonstrando como a otimização de infraestrutura tecnológica também gera impacto ambiental positivo.

No dashboard, são aplicadas regras de negócio reais, como:
- **Penalidade de Ociosidade**: Servidores com uso de CPU inferior a 20% são flagados como ociosos, gerando desperdício financeiro e penalidade na emissão de carbono (pois consomem energia sem gerar valor tangível).
- **Fatores de Emissão Regionais**: A matriz energética de cada região da AWS (`sa-east-1`, `eu-west-1`, `us-east-1`) afeta diretamente a emissão de CO₂ e o PUE médio.

---

## 🚀 Funcionalidades

### 1. 📊 Indicadores Principais (KPIs)
- **Pegada de Carbono**: Total de emissões em Toneladas (tCO₂).
- **Compensação Estimada**: Quantidade de árvores necessárias para neutralizar a emissão.
- **Desperdício Financeiro**: Custo em dólares gasto apenas com recursos ociosos.
- **PUE Médio**: Eficácia do Uso de Energia corporativa da nuvem analisada.

### 2. 📈 Visualizações Avançadas (Plotly Express)
- **Evolução Temporal das Emissões**: Gráfico de linha para acompanhar picos diários de CO₂.
- **Distribuição de Uso de CPU por Departamento**: Boxplot identificando assimetrias e servidores superdimensionados.
- **Concentração de CO₂ (Heatmap)**: Matriz de calor cruzando as Regiões AWS com os Departamentos da empresa.
- **Correlação Custo vs CO₂**: Gráfico de dispersão facetado por região AWS, mostrando o impacto ecológico por dólar gasto.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído puramente em Python, utilizando as seguintes bibliotecas:
- [Streamlit](https://streamlit.io/): Criação da interface web reativa e filtros laterais.
- [Pandas](https://pandas.pydata.org/): Manipulação, filtragem e agrupamento de dados simulados.
- [NumPy](https://numpy.org/): Geração algorítmica e pseudo-aleatória de base de dados.
- [Plotly Express](https://plotly.com/python/plotly-express/): Visualizações interativas e elaboradas com paleta temática.

---

## ⚙️ Como Executar o Projeto Localmente

**Pré-requisitos**: Python 3.10 ou superior.

1. Clone o repositório e navegue até a pasta:
```bash
git clone https://github.com/SEU_USUARIO/dashboard-ecocloud-programaria.git
cd dashboard-ecocloud-programaria
```

2. Crie e ative um ambiente virtual:
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install streamlit pandas numpy plotly
```

4. Execute o dashboard:
```bash
streamlit run app.py
```

O dashboard abrirá automaticamente no seu navegador pelo endereço `http://localhost:8501`.

---

## 💜 Agradecimentos

Este projeto é fruto dos estudos e inspirações compartilhados na **PrograMaria**, que me motivou a usar a tecnologia não apenas para fins de software, mas para pensar em sustentabilidade, métricas ESG e inovação social.

*Feito com dedicação e muito código.* ✨
