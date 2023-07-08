import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Insightly Store - Home Page",
    page_icon="✨",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------
st.markdown(
    """
<style>
    [data-testid="stSidebarNav"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------
# End Sidebar
# ---------------------------------------------------------------------

with st.container():
    header_title, home_btn = st.columns([4,1])
    with header_title:
        st.markdown("# 🔑 Login to dashboard ")

    with home_btn:
        if st.button('🏠 Home', use_container_width=True):
            switch_page("about")
        if st.button('👥 About', use_container_width=True):
            switch_page("about")
st.write("<hr>", unsafe_allow_html=True)

st.text_input("Username")
st.text_input("Password", type="password")
if st.button("Login"):
    switch_page("dashboard")