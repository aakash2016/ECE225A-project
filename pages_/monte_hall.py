import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from pages_.tag_style import get_tag_md
from simulations.monte_hall import monty_hall_simulation

custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)


def monte_hall_simulation():
    st.title("Monty Hall Problem Simulator")

    # add tags
    get_tag_md(["conditional probability", "decision making"])
    st.write("")

    st.markdown(
        """
        <div style="background-color: #D6EAF8; padding: 15px; border-radius: 10px; border: 2px solid #2980B9;">
        <p style='font-size: 16px; color: #2C3E50;'>
        This simulator demonstrates the Monty Hall problem. 
        You can choose to "stick" with your initial choice or "switch" after the host opens a door to reveal a goat.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
