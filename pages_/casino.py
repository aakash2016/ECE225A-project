# %
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from pages_.tag_style import get_tag_md
from simulations.casino import simulate_casino

custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)


def casino_simulation():
    st.title("The House Always Wins")

    # add tags
    get_tag_md(["probability", "casino"])
    st.write("")

    st.markdown(
        """
        <br/>
        <div style="background-color: #FAF3E0; padding: 15px; border-radius: 10px; border: 2px solid #C0392B;">
            <p style=color: #2C3E50;'>
                Casinos operate on the foundation of <strong>probability theory</strong>, strategically designed to ensure their long-term 
                advantage over players. In this simulation, we delve into the dynamics of gambling by allowing you to:
                <ul>
                    <li>Set your <strong>initial funds</strong>,</li>
                    <li>Decide on your <strong>wager amounts</strong>,</li>
                    <li>Control the <strong>number of bets</strong> and total games played.</li>
                </ul>
                Each bet is modeled as an independent trial with a fixed probability of winning, while the overall outcomes 
                align with the <strong>law of large numbers</strong>—highlighting that over numerous plays, the expected returns favor 
                the casino.  
                By visualizing the progression of funds over time, you'll observe how small house advantages accumulate 
                into substantial profits for the casino. This simulation not only provides insights into the mechanisms of 
                gambling but also underscores why responsible gaming is crucial. Let's explore the mathematics and see 
                why the house truly always wins! 💰
            </p>
        </div>
        <br/>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    form = st.form("MC Simulation Parameters")
    total_funds = form.slider(label='Total money in hand', min_value=500, max_value=20000, value=5000)
    wager_amount = form.slider(label='Enter the betting amount', min_value=500, max_value=total_funds, value=1000)
    num_bets = form.slider(label='Number of bets', min_value=1, max_value=1000, value=100)
    total_plays = form.slider(label='Total Plays', min_value=1, max_value=100, value=10)
    form.form_submit_button("submit")

    # line plot of funds over time
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel("Number of Bets / Play")
    ax.set_ylabel("Account Value")
    ax.set_title("Casino Simulation")

    # run simulation
    x = 1
    finalfund = []
    while x <= total_plays:
        playnum, funds, remain_funds = simulate_casino(total_funds, wager_amount, num_bets)
        finalfund.append(remain_funds)

        ax.plot(np.arange(1, num_bets+1), funds, label=f"Casino Simulation")
        x += 1

    st.write("")
    st.pyplot(fig)
    # st.write(f"the player starts the game with {total_funds} USD and ends with {int(sum(finalfund)/len(finalfund))} USD")
    message = f"""
        <br/>
        <div style="background-color: #F8D7DA; padding: 15px; border-radius: 10px; border: 2px solid #C82333;">
            <p style='font-size: 16px;'>
                The player starts the game with {total_funds} USD and ends with {int(sum(finalfund)/len(finalfund))} USD.
            </p>
        </div>
    """
    # Render in Streamlit
    st.markdown(message, unsafe_allow_html=True)
