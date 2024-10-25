# $

import streamlit as st

from simulations.casino import simulate_casino


def main():
    # ui-configurations
    st.title("Simulator")
    # st.sidebar.title("Choose a game to simulate")
    option = st.sidebar.radio("Select a simulation:", ('casino', 'poker', 'monte_hall', 'insurance_claims'))

    if option == 'casino':
        form = st.form("Parameters")
        total_funds = form.slider(label='Total money in hand', min_value=500, max_value=20000, value=2000)
        wager_amount = form.slider(label='Enter the betting amount', min_value=500, max_value=total_funds, value=1000)
        total_plays = form.slider(label='Number of games', min_value=1, max_value=100, value=10)
        form.form_submit_button("submit")

        # run simulation
        remain_funds = simulate_casino(total_funds, wager_amount, total_plays)
        st.write(f"{remain_funds}")
    elif option == 'Poker':
        pass
    elif option == 'monte_hall':
        st.write("monte_hall")
    elif option == 'insurance_claims':
        st.write("insurance_claims")


if __name__ == "__main__":
    main()
