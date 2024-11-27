import streamlit as st

# Define custom CSS for tags
st.markdown(
    """
    <style>
    .tag {
        color: white;
        background-color: green;
        border-radius: 8px;
        padding: 5px 10px;
        font-size: 14px;
        margin: 5px;
        display: inline-block;
        float: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the tags on the right side
def get_tag_md(tags):
    tag_html = "".join(
        f'<span class="tag">{tag}</span>' for tag in tags
    )

    st.markdown(
        f"""
        <style>
        .tag {{
            color: white;
            background-color: green;
            border-radius: 8px;
            padding: 5px 10px;
            font-size: 14px;
            margin-right: 5px;
            display: inline-block;
        }}
        </style>
        <div style="text-align: left;">
            {tag_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
