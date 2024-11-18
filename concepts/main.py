import streamlit as st
from pages_.intro import intro
from gaussian import plot_sum_gaussian
from clt import plot_clt
from binomial_to_poisson import plot_binomial_to_poisson

page_names_to_funcs = {
    "—": intro,
    "Sum of 2 gaussians": plot_sum_gaussian,
    "Central Limit Theorem": plot_clt,
    "Binomial-poisson": plot_binomial_to_poisson
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()