# Save this file as `binomial_poisson_approximation.py` and run with `streamlit run binomial_poisson_approximation.py`

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

st.title("Binomial Distribution Approximating a Poisson Distribution")

st.write("""
As \( n \) becomes large and \( p \) becomes small such that \( n \cdot p \) is constant, 
the binomial distribution \( \text{Binomial}(n, p) \) approximates a Poisson distribution with parameter \( \lambda = n \cdot p \).
This simulator allows you to adjust the values of \( n \) and \( p \) and observe the approximation.
""")

# Controls for the binomial parameters n and p
n = st.slider("Number of trials (n)", min_value=10, max_value=1000, value=100, step=10)
p = st.slider("Probability of success (p)", min_value=0.01, max_value=1.0, value=0.5, step=0.05)

# Calculate lambda for the Poisson distribution
lambda_ = n * p

# Generate x-axis range based on lambda
x_values = np.arange(0, max(15, int(lambda_ + 4 * np.sqrt(lambda_))))  # Dynamically adjust the x-axis range

# Calculate binomial and Poisson probabilities
binomial_probs = binom.pmf(x_values, n, p)
poisson_probs = poisson.pmf(x_values, lambda_)

# Plotting the distributions
fig, ax = plt.subplots()
ax.bar(x_values - 0.2, binomial_probs, width=0.4, color="blue", label="Binomial PMF", alpha=0.6)
ax.bar(x_values + 0.2, poisson_probs, width=0.4, color="red", label="Poisson PMF", alpha=0.6)

# Labels and legend
ax.set_title(f"Binomial (n={n}, p={p}) vs Poisson (λ={lambda_:.2f})")
ax.set_xlabel("Number of Successes")
ax.set_ylabel("Probability")
ax.legend()

# Display the plot
st.pyplot(fig)

# Additional insights
st.write(f"For n={n} and p={p}, the equivalent λ (mean of Poisson) is {lambda_:.2f}.")
st.write("Observe that as n increases and p decreases, the binomial distribution approximates the Poisson distribution more closely.")
