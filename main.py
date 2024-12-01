import streamlit as st
from pages_.intro import intro
from pages_.casino import casino_simulation
from pages_.poker_sim import poker_simulation
from pages_.monte_hall import monte_hall_simulation
from pages_.insurance import insurance_simulation
from pages_.wait_times import hospital_wait_time_simulation
from concepts.gaussian import plot_sum_gaussian
from concepts.clt import plot_clt
from concepts.binomial_to_poisson import plot_binomial_to_poisson

# Mapping pages to functions
# Mapping pages to functions
page_names_to_funcs_demo = {
    "—": intro,
    "🎰 Casino": casino_simulation,
    "🃏 Poker": poker_simulation,
    "🎲 Monte Hall": monte_hall_simulation,
    "💡 Insurance": insurance_simulation,
    "⏳ Wait Times": hospital_wait_time_simulation,
}

page_names_to_funcs_concepts = {
    "—": intro,
    "📊 Sum of 2 Gaussians": plot_sum_gaussian,
    "📉 Central Limit Theorem": plot_clt,
    "🔢 Binomial-Poisson": plot_binomial_to_poisson,
}

# Sidebar selection
st.sidebar.title("✨ **Course Project: Probability & Statistics for Data Science** 📚")
category = st.sidebar.radio("🔍 **Choose a category**", ["🔬 Demo", "📚 Appendix"])

if category == "🔬 Demo":
    demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs_demo.keys())
    page_names_to_funcs_demo[demo_name]()
elif category == "📚 Appendix":
    concept_name = st.sidebar.selectbox("Choose a concept", page_names_to_funcs_concepts.keys())
    page_names_to_funcs_concepts[concept_name]()