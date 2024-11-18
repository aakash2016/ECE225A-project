# %

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)

from simulations.casino import simulate_casino


def casino_simulation():
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
