import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ============================================================
# CONFIGURACIÓN INICIAL
# ============================================================
st.set_page_config(page_title="University Data Dashboard", layout="wide")
st.title("📊 University Analytics Dashboard")
st.markdown("Análisis de Admisión, Retención y Satisfacción Estudiantil")

# ============================================================
# CARGAR LOS DATOS
# ============================================================
df = pd.read_csv("university_student_data.csv")

# ============================================================
# FILTROS INTERACTIVOS
# ============================================================
st.sidebar.header("Filtros")

# Filtro por año
years = sorted(df["Year"].unique())
selected_years = st.sidebar.multiselect("Selecciona año(s):", years, default=years)

# Filtro por semestre
terms = df["Term"].unique()
selected_terms = st.sidebar.multiselect("Selecciona semestre(s):", terms, default=terms)

# Aplicar filtros
filtered_df = df[(df["Year"].isin(selected_years)) & (df["Term"].isin(selected_terms))]

# ============================================================
# INDICADORES CLAVE (KPI)
# ============================================================
st.subheader("📈 Indicadores Clave")
col1, col2, col3 = st.columns(3)
col1.metric("Retención Promedio (%)", f"{filtered_df['Retention Rate (%)'].mean():.1f}")
col2.metric("Satisfacción Promedio (%)", f"{filtered_df['Student Satisfaction (%)'].mean():.1f}")
col3.metric("Matrícula Promedio", f"{filtered_df['Enrolled'].mean():.0f}")

st.markdown("---")

# ============================================================
# GRÁFICO 1: Tendencia de la Tasa de Retención
# ============================================================
st.subheader("Tendencia de la Tasa de Retención (%)")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered_df, x="Year", y="Retention Rate (%)", hue="Term", marker="o", ax=ax1)
st.pyplot(fig1)

# ============================================================
# GRÁFICO 2: Satisfacción por Año
# ============================================================
st.subheader("Satisfacción Estudiantil Promedio por Año")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered_df, x="Year", y="Student Satisfaction (%)", hue="Term", ax=ax2, palette="Blues_d")
st.pyplot(fig2)

# ============================================================
# GRÁFICO 3: Distribución de Matrículas por Departamento
# ============================================================
st.subheader("Distribución de Matrículas por Departamento")
dept_data = filtered_df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
fig3, ax3 = plt.subplots()
dept_data.plot(kind="pie", autopct="%1.1f%%", ax=ax3, ylabel="")
st.pyplot(fig3)

