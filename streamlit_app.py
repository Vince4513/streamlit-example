import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from rules import Rules

st.set_page_config(
    page_title="Stock Analysis",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title("Stock Analysis Dashboard")
st.markdown("_Prototype v0.1.0_")

raw_data_tab, kpi_tab, rules_tab = st.tabs(["Upload", "KPI", "7 Rules"])

with st.sidebar:
    st.page_link("streamlit_app.py", label="Home page", icon="🏠")
    st.page_link("https://www.boursorama.com/bourse/actions/palmares/dividendes/", label="Boursorama", icon="🌎")
    st.page_link("https://finary.com/fr", label="Finary", icon="🌎")
    # st.page_link("https://www.boursorama.com/bourse/actions/palmares/dividendes/", label="Boursorama", icon="🌎")

with raw_data_tab:
    st.header("Raw data")
    @st.cache_data
    def load_data(file):
        data = pd.read_excel(file)
        return data

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is None:
        st.info("Upload a file through config")
        # st.stop()

    # df = load_data(uploaded_file) 

    share_actual_price = [25, 25, 20]

with kpi_tab:
    st.header("KPI")
    
    # Define sample data for multiple companies
    data = {
        'Company': ['Orange', 'Total', 'Nexity'],
        'Sales': [1000000, 1500000, 800000],
        'Current assets': [500000, 700000, 400000],
        'Current liabilities': [200000, 300000, 250000],
        'Financial debts': [300000, 200000, 150000],
        'Number of shares issued': [10000, 1500000, 800000],
        'Shareholders\' equity': [1000000, 1500000, 800000],
        'Intangible assets': [10000, 1500, 8000],
        'Net income 1 year': [150000, 200000, 100000],
        'Net income 2 year': [120000, 180000, 90000],
        'Net income 3 year': [130000, 190000, 95000],
        'Net income 4 year': [150000, 200000, 100000],
        'Net income 5 year': [120000, 180000, 90000],
        'Net income 6 year': [130000, -190000, 95000],
        'Net income 7 year': [150000, 200000, 100000],
        'Net income 8 year': [120000, 180000, 90000],
        'Net income 9 year': [130000, 190000, 95000],
        'Net income 10 year': [130000, 190000, 95000],
        'Dividends 1 year': [1.5, 2, 1],
        'Dividends 2 year': [1.2, 1.8, 0.9],
        'Dividends 3 year': [1.3, 1.9, 0.95],
        'Dividends 4 year': [1.5, 2, 1],
        'Dividends 5 year': [1.2, 1.8, 0.9],
        'Dividends 6 year': [1.3, 1.9, 0.95],
        'Dividends 7 year': [1.5, 2, 1],
        'Dividends 8 year': [1.2, 1.8, 0.9],
        'Dividends 9 year': [1.3, 1.9, np.nan],
        'Dividends 10 year': [1.3, 1.9, 0.95],
        'Net earnings per share 1 year': [1.5, 2.0, 1.0],
        'Net earnings per share 2 year': [1.5, 2.1, 1.1],
        'Net earnings per share 3 year': [1.5, 2.2, 1.2],
        'Net earnings per share 4 year': [1.0, 1.0, 1.0],
        'Net earnings per share 5 year': [1.0, 1.0, 1.0],
        'Net earnings per share 6 year': [1.0, 1.0, 1.0],
        'Net earnings per share 7 year': [1.0, 1.0, 1.0],
        'Net earnings per share 8 year': [1.7, 1.5, 1.8],
        'Net earnings per share 9 year': [1.8, 1.4, 1.9],
        'Net earnings per share 10 year': [1.9, 1.3, 1.9]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    st.dataframe(df)  
   
with rules_tab:
    st.header("7 Rules")

    Rule = Rules(share_actual_price)
    Rule.determine_measures(df)
    Rule.determine_rules(df)
    st.dataframe(Rule.df_rules)
    st.write(Rule.PER, Rule.PBR)

