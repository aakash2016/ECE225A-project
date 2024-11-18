import streamlit as st
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from simulations.insurance import simulate_insurance

custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)


def insurance_simulation():
    st.title("Underwriting Profits: The Hidden Dynamics of Insurance Success")

    # User inputs
    num_years = st.slider("Number of years", min_value=1, max_value=10, value=1)
    num_policies = st.slider("Number of Policies", min_value=10, max_value=500, step=10, value=100)
    num_simulations = st.slider("Number of Simulations", min_value=1000, max_value=50000, value=10000)

    # Run simulation
    if st.button("Run Simulation"):
        # Run simulation multiple times
        results = [simulate_insurance(num_policies, num_years) for _ in range(num_simulations)]

        # Analyze results
        average_profit = np.mean(results)
        profit_probability = np.sum(np.array(results) > 0) / num_simulations

        st.write(f"Average annual profit: ${average_profit:.2f}")
        st.write(f"Probability of making a profit: {profit_probability:.2%}")

        # Plot histogram of results
        plt.hist(results, bins=50)
        plt.title("Distribution of Annual Profits")
        plt.xlabel("Profit ($)")
        plt.ylabel("Frequency")
        st.pyplot(plt)
