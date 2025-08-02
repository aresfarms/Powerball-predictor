
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos Powerball Predictor", layout="wide")
st.title("🎯 Chaos Powerball Predictor")

st.markdown("""
Welcome to the Powerball Predictor app. This tool provides:
- Statistically significant number suggestions
- Probability-based match checking
- Historical win data for red and white balls
- Layman-friendly odds output
""")

# Load CSV files
white_df = pd.read_csv("white_ball_stats.csv")
red_df = pd.read_csv("red_ball_stats.csv")
odds_df = pd.read_csv("powerball_odds_table.csv")

# Display probability tables
st.subheader("📊 White Ball Probability Table")
st.dataframe(white_df)

st.subheader("📕 Red Ball Probability Table")
st.dataframe(red_df)

st.subheader("🎲 Powerball Odds Table")
st.dataframe(odds_df)

# Odds calculator
st.markdown("---")
st.subheader("🔢 Winning Odds Calculator")

white_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
red_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, value=1)
calc = st.button("Calculate Winning Odds")

def calculate_odds(white_balls, powerball):
    white_balls = [int(x.strip()) for x in white_balls.split(",") if x.strip().isdigit()]
    if len(white_balls) != 5:
        return "Please enter exactly 5 unique white balls."
    return "1 in 292,201,338 (0.00000034%) - National Powerball Jackpot Odds"

if calc:
    result = calculate_odds(white_input, red_input)
    st.success(result)
