import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from simulations.insurance import simulate_insurance
from pages_.tag_style import get_tag_md

custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)


def insurance_simulation():
    st.title("Underwriting Profits: The Hidden Dynamics of Insurance Success")

    # add tags
    get_tag_md(["binomial distribution", "profit"])
    st.write("")
    st.markdown(
        """
        <div style="background-color: #F9F9F9; padding: 15px; border-radius: 10px; border: 2px solid #3498DB;">
            <p style='font-size: 18px; color: #2C3E50;'>
                Welcome to the <strong>Insurance Profit Simulator</strong>! 🏦 This interactive tool explores the hidden dynamics behind 
                underwriting profits, where mathematics and probability come together to drive success in the insurance 
                industry. At its core, this simulation leverages concepts from the <strong>binomial distribution</strong> to model the 
                outcomes of insurable events. By simulating we can estimate two key metrics:
                <ul>
                    <li>The <strong>average annual profit</strong>, offering insights into the company's performance.</li>
                    <li>The <strong>probability of making a profit</strong>, providing a measure of risk and sustainability.</li>
                </ul>
                With this simulator, you can adjust variables such as the number of policies, years, and simulation runs to 
                understand how small changes in assumptions impact the overall profitability. By analyzing the results, 
                you'll gain a deeper appreciation of how probability-driven strategies influence real-world decisions in 
                the insurance industry.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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

        message = f"""
                <div style="background-color: #94F9F3; padding: 15px; border-radius: 10px; border: 2px solid #2980B9;">
                    <p style='font-size: 16px; color: #2C3E50;'>
                        Average annual profit: ${average_profit:.2f} <br>
                        Probability of making a profit: {profit_probability:.2%}
                    </p>
                </div>
            """
        # Render in Streamlit
        st.markdown(message, unsafe_allow_html=True)

        # Plot histogram of results
        plt.hist(results, bins=50)
        plt.title("Distribution of Annual Profits")
        plt.xlabel("Profit ($)")
        plt.ylabel("Frequency")
        st.pyplot(plt)
