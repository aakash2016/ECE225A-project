import streamlit as st
from pages.intro import intro
from pages.casino import casino_simulation
from pages.poker_sim import poker_simulation
from pages.monte_hall import monte_hall_simulation

# from gaussian import plot_sum_gaussian
# from clt import plot_clt
# from binomial_to_poisson import plot_binomial_to_poisson


page_names_to_funcs = {
    "—": intro,
    "Casino": casino_simulation,
    "Poker": poker_simulation,
    "Monte Hall": monte_hall_simulation
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()