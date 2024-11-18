import streamlit as st
from pages_.intro import intro
from pages_.casino import casino_simulation
from pages_.poker_sim import poker_simulation
from pages_.monte_hall import monte_hall_simulation


page_names_to_funcs = {
    "—": intro,
    "Casino": casino_simulation,
    "Poker": poker_simulation,
    "Monte Hall": monte_hall_simulation
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()