def intro():
    import streamlit as st

    # Title with styling
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1;'>🚀 Course Project - ECE-225A - Probability & Statistics for Data Science 📊</h1>
        <br/>
        """,
        unsafe_allow_html=True,
    )

    # Project Description
    st.markdown(
        """
        <div style="background-color: #F9EBEA; padding: 15px; border-radius: 10px; border: 2px solid #E74C3C;">
        <p style='font-size: 16px; color: #2C3E50;'>
        This project is a hands-on journey into the fascinating world of probability and statistics, where theory meets practical insights.
        We bring complex ideas to life through engaging simulations and interactive visualizations, designed to make learning <strong>fun</strong>, <strong>intuitive</strong>, and <strong>informative</strong>.
        </p>
        </div>
        <br/>
        """,
        unsafe_allow_html=True,
    )

    # What Will We Cover? Section
    st.markdown(
        """
        ### 🔍 **What Will We Cover?**
        Dive into the following exciting topics:
        - 🎰 **The House Always Wins (Casino)**: Explore probabilities through Monte Carlo simulations.
        - 🃏 **Poker Game Simulation**: Analyze probabilities in a competitive card game.
        - 🚪 **Monte Hall Problem Simulation**: Unveil the counterintuitive probabilities behind this classic puzzle.
        - 🏦 **Insurance Profit-Making Simulation**: Understand risk analysis and profit models.
        - 🏥 **Hospital Wait Time Simulation**: Witness the power of the Central Limit Theorem (CLT) in action.
        """
    )

    # Appendix Section
    st.markdown(
        """
        ### 📘 **Appendix: Core Concepts**
        We also provide interactive modules to deepen your understanding of key statistical concepts:
        - 🧮 **Poisson as an Approximation to Binomial Distribution**: Grasp when and why this works.
        - 📉 **Sum of Two Gaussian Distributions**: Visualize why their sum is still a Gaussian.
        - 🔄 **Central Limit Theorem**: Discover why averages follow a normal distribution as sample sizes grow.
        """
    )

    # Team Members Section
    st.markdown(
        """
        ### 👨‍🎓 **Team Members**
        Meet the brilliant minds behind this project:
        - **Rishabh Thapliyal**
        - **Aakash Agrawal**
        """
    )

    # Closing Motivation
    st.markdown(
        """
        <br/>
        <div style="background-color: #D6EAF8; padding: 15px; padding-left: 15px; padding-right: 15px; border-radius: 10px; border: 2px solid #2980B9; text-align: center; width: fit-content; margin: auto;">
        <p style='font-size: 16px; color: #2C3E50;'>
            Let’s explore the world of <strong>Probability & Statistics</strong> together! 🚀
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

