import streamlit as st
from scraper import get_latest_numbers
from utils import calculate_odds, display_tables

st.title("Powerball Predictor")

user_numbers = st.text_input("Enter your numbers (comma-separated):", "")
if st.button("Check My Numbers"):
    try:
        latest_draw = get_latest_numbers()
        odds, result = calculate_odds(user_numbers, latest_draw)
        st.write(f"Your odds: {odds}")
        st.write(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

display_tables()
