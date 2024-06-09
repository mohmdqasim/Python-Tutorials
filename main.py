import streamlit as st
from streamlit_option_menu import option_menu

from Learning import learn
from Assignment import assignment

pages = {
    "Learn": learn,
    "Assignments": assignment,
}

with st.sidebar:
    selected = option_menu(
        menu_title = "Learn Python",
        options = list(pages.keys()),
        icons = ["house", "person-arms-up", "book"],
        menu_icon = "robot",
        default_index = 0
    )

pages[selected]()