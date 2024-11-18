def intro():
    import streamlit as st

    st.markdown("<h1 style='text-align: center; color: black;'>Course Project 💻</h1>", unsafe_allow_html=True)
    # st.title("Course Project! :computer:")
    st.write("#### ECE 225: Probability and Statistics for Data Science! :chart_with_upwards_trend:")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        We aim to demonstrate key concepts discussed in the class through interactive examples, making complex ideas easier to understand and interpret.

        ### What will we cover?
        - Monte Carlo Simulation



        
        ### Team members

        - Rishabh Thapliyal
        - Aakash Agarwal
    """
    )