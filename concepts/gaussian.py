# Save this file as `sum_of_gaussians.py` and run with `streamlit run sum_of_gaussians.py`

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

st.title("Sum of Two Gaussian Distributions")

# Select parameters for the first Gaussian distribution
st.sidebar.header("Parameters for Distribution 1")
mean1 = st.sidebar.slider("Mean of Distribution 1", -10.0, 10.0, 0.0)
variance1 = st.sidebar.slider("Variance of Distribution 1", 0.1, 10.0, 1.0)
std_dev1 = np.sqrt(variance1)

# Select parameters for the second Gaussian distribution
st.sidebar.header("Parameters for Distribution 2")
mean2 = st.sidebar.slider("Mean of Distribution 2", -10.0, 10.0, 0.0)
variance2 = st.sidebar.slider("Variance of Distribution 2", 0.1, 10.0, 1.0)
std_dev2 = np.sqrt(variance2)

# Create the x-axis range for the plot
x = np.linspace(-20, 20, 1000)

# Calculate the individual Gaussian distributions
dist1 = norm.pdf(x, mean1, std_dev1)
dist2 = norm.pdf(x, mean2, std_dev2)

# Sum of the two Gaussian distributions
mean_sum = mean1 + mean2
variance_sum = variance1 + variance2
std_dev_sum = np.sqrt(variance_sum)
dist_sum = norm.pdf(x, mean_sum, std_dev_sum)

# Plot all three distributions
fig, ax = plt.subplots()
ax.plot(x, dist1, label=f"Dist 1: Mean={mean1}, Variance={variance1}", color="blue")
ax.plot(x, dist2, label=f"Dist 2: Mean={mean2}, Variance={variance2}", color="green")
ax.plot(x, dist_sum, label=f"Sum: Mean={mean_sum}, Variance={variance_sum}", color="red", linestyle="--")

# Add labels and legend
ax.set_title("Gaussian Distributions and Their Sum")
ax.set_xlabel("X")
ax.set_ylabel("Probability Density")
ax.legend()

# Display the plot
st.pyplot(fig)
