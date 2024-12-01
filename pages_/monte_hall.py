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
            <p style='font-size: 14px; color: #2C3E50;'>
            The Monty Hall problem is a classic probability puzzle based on a game show. Imagine there are three doors:
            - Behind one door is a <strong>car</strong> (the prize you want to win 🚗).
            - Behind the other two doors are <strong>goats</strong> (not the prize 🐐).  
            </p>
            <p style='font-size: 14px; color: #2C3E50;'>
            Here's how it works:
            1. You make an initial choice by selecting one of the three doors. 🚪
            2. The host, Monty Hall (who knows what's behind each door), opens another door, revealing a goat. 🐐
            3. You now have two options: 
                - <strong>Stick</strong> with your original choice.
                - <strong>Switch</strong> to the other unopened door.  
            </p>
            <p style='font-size: 14px; color: #2C3E50;'>
            <strong>🧠 The Probability Insight</strong>
            - If you <strong>stick</strong> with your original choice, your probability of winning the car remains <strong>1/3</strong> (since you had a 1 in 3 chance initially).
            - If you <strong>switch</strong>, your probability of winning becomes <strong>2/3</strong>. Why? When Monty opens a door to reveal a goat, he provides additional information, effectively doubling your odds of winning by switching!
            </p>
            <p style='font-size: 14px; color: #2C3E50;'>
            This simulator lets you test these probabilities by simulating multiple rounds of the game. 
            Observe how switching consistently gives you better odds over many iterations. 🎲✨
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
