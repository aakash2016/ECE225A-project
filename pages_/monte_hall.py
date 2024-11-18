def monte_hall_simulation():
    import streamlit as st
    import matplotlib.pyplot as plt
    import sys
    sys.path.append('../simulations')
    from simulations.monte_hall import monty_hall_simulation

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

    return