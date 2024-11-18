# $

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from simulations.casino import simulate_casino
from simulations.monte_hall import monty_hall_simulation


custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)


def main():
    # ui-configurations
    # st.sidebar.title("Choose a game to simulate")
    option = st.sidebar.radio("Select a simulation:", ('casino', 'poker', 'monte_hall', 'insurance_claims'))

    if option == 'casino':
        st.title("The House Always Wins")

        form = st.form("MC Simulation Parameters")
        total_funds = form.slider(label='Total money in hand', min_value=500, max_value=20000, value=5000)
        wager_amount = form.slider(label='Enter the betting amount', min_value=500, max_value=total_funds, value=1000)
        num_bets = form.slider(label='Number of bets', min_value=1, max_value=1000, value=100)
        total_plays = form.slider(label='Total Plays', min_value=1, max_value=100, value=10)
        form.form_submit_button("submit")

        # line plot of funds over time
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlabel("Total Plays")
        ax.set_ylabel("Account Value")
        ax.set_title("Casino Simulation")

        # run simulation
        x = 1
        finalfund = []
        while x <= total_plays:
            playnum, funds, remain_funds = simulate_casino(total_funds, wager_amount, num_bets)
            finalfund.append(remain_funds)

            ax.plot(playnum, funds, label=f"Casino Simulation")
            x += 1

        st.pyplot(fig)
        st.write(f"the player starts the game with {total_funds} USD and ends with {int(sum(finalfund)/len(finalfund))} USD")

    elif option == 'monte_hall':
        # Streamlit app layout
        st.title("Monty Hall Problem Simulator")
        st.write("""
            This simulator demonstrates the Monty Hall problem. 
            You can choose to "stick" with your initial choice or "switch" after the host opens a door to reveal a goat.
        """)

        # User inputs
        num_trials = st.slider("Number of Trials", min_value=100, max_value=10000, step=100, value=1000)
        switch = st.radio("Would you like to switch doors?", ("Yes", "No"))

        # Run simulation
        if st.button("Run Simulation"):
            wins, win_history = monty_hall_simulation(num_trials, switch == "Yes")
            win_percentage = (wins / num_trials) * 100

            # Display results
            st.write(f"**Trials:** {num_trials}")
            st.write(f"**Wins:** {wins}")
            st.write(f"**Win Percentage:** {win_percentage:.2f}%")
            if switch == "Yes":
                st.write("**Strategy**: Switching doors")
            else:
                st.write("**Strategy**: Sticking with the initial choice")

            # Plotting win rate over trials
            plt.figure(figsize=(10, 5))
            plt.plot(range(1, num_trials + 1), win_history, label="Win Rate")
            plt.axhline(y=2 / 3 if switch == "Yes" else 1 / 3, color="r", linestyle="--", label="Expected Win Rate")
            plt.xlabel("Number of Trials")
            plt.ylabel("Win Rate")
            plt.title("Win Rate Over Time")
            plt.legend()
            st.pyplot(plt)

    elif option == 'insurance_claims':
        st.write("insurance_claims")


if __name__ == "__main__":
    main()
