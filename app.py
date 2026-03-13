import streamlit as st
import sys
import io
import pandas as pd

def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys.stdout = buffer
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = sys.__stdout__
    return buffer.getvalue()

from print_top_100_all_time_worldwide import print_top_100_all_time_worldwide
from print_top_50_2025 import print_top_50_2025
from print_top_50_2026 import print_top_50_2026
from print_five_million_watched_club import print_five_million_watched_club

st.set_page_config(page_title="Box Office Stats", page_icon="🎬", layout="wide")
st.title("Stats Automator")

tab1, tab2, tab3, tab4 = st.tabs([
    "Top 100 All-Time Worldwide",
    "Top 50 - 2025",
    "Top 50 - 2026",
    "Five Million Watched Club"
])

with tab1:
    st.subheader("Top 100 All-Time Worldwide Box Office")
    if st.button("Load Stats", key="btn1"):
        with st.spinner("Fetching data..."):
            output = capture_output(print_top_100_all_time_worldwide)
        st.text(output)

with tab2:
    st.subheader("2025 Worldwide Box Office — Top 50")
    if st.button("Load Stats", key="btn2"):
        with st.spinner("Fetching data..."):
            output = capture_output(print_top_50_2025)
        st.text(output)

with tab3:
    st.subheader("2026 Worldwide Box Office — Top 50")
    if st.button("Load Stats", key="btn3"):
        with st.spinner("Fetching data..."):
            output = capture_output(print_top_50_2026)
        st.text(output)

with tab4:
    st.subheader("Letterboxd Five Million Watched Club")
    if st.button("Load Stats", key="btn4"):
        with st.spinner("Fetching data..."):
            output = capture_output(print_five_million_watched_club)
        st.text(output)