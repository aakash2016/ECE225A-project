import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the title and description
st.title("Central Limit Theorem Simulation")
st.write("""
The Central Limit Theorem (CLT) states that the distribution of sample means approaches a normal distribution as the sample size increases, regardless of the original distribution.
""")

# Sidebar inputs for distribution type, sample size, and number of samples
distribution_type = st.sidebar.selectbox(
    "Select the Distribution Type",
    ["Uniform", "Exponential", "Binomial"]
)

sample_size = st.sidebar.slider("Sample Size (n)", min_value=10, max_value=1000, value=30, step=10)
num_samples = st.sidebar.slider("Number of Samples", min_value=100, max_value=5000, value=1000, step=100)

# Generate data based on the selected distribution
if distribution_type == "Uniform":
    original_data = np.random.uniform(0, 1, num_samples * sample_size)
    data_title = "Uniform Distribution (0, 1)"
elif distribution_type == "Exponential":
    original_data = np.random.exponential(scale=1, size=num_samples * sample_size)
    data_title = "Exponential Distribution (λ=1)"
elif distribution_type == "Binomial":
    original_data = np.random.binomial(n=10, p=0.5, size=num_samples * sample_size)
    data_title = "Binomial Distribution (n=10, p=0.5)"

# Reshape the data into an array of samples of size `sample_size`
sampled_data = original_data.reshape(num_samples, sample_size)

# Calculate the sample means
sample_means = sampled_data.mean(axis=1)

# Plot the original distribution and the sample mean distribution
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot the original data distribution
sns.histplot(original_data, kde=True, ax=ax[0], bins=30, color="skyblue")
ax[0].set_title(f"Original {data_title}")
ax[0].set_xlabel("Value")
ax[0].set_ylabel("Frequency")

# Plot the distribution of the sample means
sns.histplot(sample_means, kde=True, ax=ax[1], bins=30, color="salmon")
ax[1].set_title(f"Distribution of Sample Means (n={sample_size})")
ax[1].set_xlabel("Sample Mean")
ax[1].set_ylabel("Frequency")

# Display the plot in Streamlit
st.pyplot(fig)

# Additional explanations
st.write(f"With sample size {sample_size} and {num_samples} samples, observe how the distribution of sample means resembles a normal distribution even though the original data follows a {distribution_type} distribution.")
