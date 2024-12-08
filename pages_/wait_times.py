import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from pages_.tag_style import get_tag_md
from simulations.wait_times import mean_wait_time

custom = {"axes.edgecolor": "red", "grid.linestyle": "dashed", "grid.color": "black"}
sns.set_style("darkgrid", rc=custom)


def hospital_wait_time_simulation():
    # Streamlit interface for user input
    st.title("Hospital Wait Time Simulation with Central Limit Theorem")

    # add tags
    get_tag_md(["exponential distribution", "uniform distribution", "CLT"])
    st.write("")
    st.write("")
    st.markdown(
        """
        <br/>
        <div style="background-color: #F9F9F9; padding: 15px; border-radius: 10px; border: 2px solid #3498DB;">
            <p style='font-size: 18px; color: #2C3E50;'>
                Patient arrival time is distributed uniformly.
                Average service rate (time between treating 2 patients) is distributed exponentially
                with mean as 1/ƛ.
                Average wait time for multiple simulations follow normal distribution.
            </p>
        </div>
        <br/>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    # Interactive range slider for controlling both arrival_rate_min and arrival_rate_max
    arrival_rate = st.slider(
        "Select Arrival Rate Range (patients per minute)",
        min_value=1, max_value=20, value=(1, 10), step=1,
        format="%.1f"
    )

    # Extract the min and max values from the range slider
    arrival_rate_min, arrival_rate_max = arrival_rate

    # Interactive sliders for other parameters
    num_patients = st.slider("Number of patients", min_value=100, max_value=1000, value=500, step=100)
    service_rate = st.slider("Average Service rate (minutes per patient (1/ƛ) )", 0.1, 2.0, 0.7, 0.1)
    num_simulations = st.slider("Number of simulation runs", 100, 5000, 1000, 100)

    # Run simulation
    if st.button("Run Simulation"):
        # Simulate patient wait times
        wait_times = []
        for _ in range(num_simulations):
            mwt = mean_wait_time(num_patients, service_rate, arrival_rate_min, arrival_rate_max)
            wait_times.append(mwt)

        # Convert list to numpy array
        wait_times = np.array(wait_times)

        # Plot histogram of average wait times
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(wait_times, bins=30, color='purple', edgecolor='black', alpha=0.7)
        ax.axvline(np.mean(wait_times), color='red', linestyle='dashed', linewidth=2,
                   label=f"Mean: {np.mean(wait_times):.2f}")
        ax.axvline(np.mean(wait_times) + np.std(wait_times), color='blue', linestyle='dashed', linewidth=2,
                   label=f"1 Std Dev: {np.mean(wait_times) + np.std(wait_times):.2f}")
        ax.axvline(np.mean(wait_times) - np.std(wait_times), color='blue', linestyle='dashed', linewidth=2)
        ax.set_title("Hospital Wait Time Simulation with Central Limit Theorem")
        ax.set_xlabel("Average Wait Time (minutes)")
        ax.set_ylabel("Frequency")
        ax.legend()

        # Display the plot
        st.pyplot(fig)

        # Display statistics
        # st.write(f"**Mean Wait Time:** {np.mean(wait_times):.2f} minutes")
        # st.write(f"**Standard Deviation of Wait Time:** {np.std(wait_times):.2f} minutes")
        # st.write(f"**Probability of waiting > 60 minutes:** {np.sum(wait_times > 60) / num_simulations:.2f}")
        message = f"""
            <div style="background-color: #FBECF7; padding: 15px; border-radius: 10px; border: 2px solid #2980B9;">
                <p style='font-size: 16px; color: #2C3E50;'>
                    <b>Mean Wait Time:</b> {np.mean(wait_times):.2f} minutes<br>
                    <b>Standard Deviation of Wait Time:</b> {np.std(wait_times):.2f} minutes<br>
                </p>
            </div>
        """

        # <b>Probability of waiting > 60 minutes:</b> {np.sum(wait_times > 60) / num_simulations:.2f}
        # Render in Streamlit
        st.markdown(message, unsafe_allow_html=True)