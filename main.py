# $

import streamlit as st

from simulations.casino import simulate_casino


def main():
    # ui-configurations
    st.title("Simulator")
    # st.sidebar.title("Choose a game to simulate")
    option = st.sidebar.radio("Select a simulation:", ('casino', 'poker', 'monte_hall', 'insurance_claims'))

    if option == 'casino':
        remain_funds = simulate_casino(10000, 100, 1000)
        st.write(f"{remain_funds}")
    elif option == 'Poker':
        pass
    elif option == 'monte_hall':
        st.write("monte_hall")
    elif option == 'insurance_claims':
        st.write("insurance_claims")


if __name__ == "__main__":
    main()
