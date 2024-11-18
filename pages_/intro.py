def intro():
    import streamlit as st

    st.markdown("<h1 style='text-align: center; color: black;'>Course Project 💻</h1>", unsafe_allow_html=True)
    # st.title("Course Project! :computer:")
    st.write("#### ECE 225: Probability and Statistics for Data Science! :chart_with_upwards_trend:")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        We aim to demonstrate key class concepts through interactive examples, making complex ideas easier to understand and interpret.

        ### What will we cover?

        - Sum of Two Gaussians: Showing how the sum of two Gaussian distributions results in another Gaussian.
        - Central Limit Theorem: Illustrating how this fundamental statistical principle works in practice.
        - Poisson Distribution as a Special Case of Binomial Distribution: Demonstrating how the Poisson distribution emerges from the binomial distribution under certain conditions.
        
        ### Team members

        - Rishabh Thapliyal
        - Aakash Agarwal
    """
    )