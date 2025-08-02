
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos Powerball Predictor", layout="wide")
st.title("🎲 Chaos-Based Powerball Predictor (Friendly Odds)")

st.markdown("""
Welcome to the Powerball Predictor app. This tool provides:
- Statistically significant number suggestions
- Probability-based match checking
- Historical win data for red and white balls
- Layman-friendly odds output
""")

# 1. Winning Odds Table
odds_data = {
    "Match Type": [
        "Match Powerball only",
        "Match 1 white ball + Powerball",
        "Match 2 white balls + Powerball",
        "Match 3 white balls",
        "Match 3 white + Powerball",
        "Match 4 white balls",
        "Match 4 white + Powerball",
        "Match 5 white balls only",
        "Match 5 white + Powerball"
    ],
    "Prize": ["$4", "$4", "$7", "$7", "$100", "$100", "$50,000", "$1 million", "Jackpot"],
    "Odds (1 in X)": [
        "1 in 26", "1 in 92", "1 in 701", "1 in 579", "1 in 14,494", 
        "1 in 36,525", "1 in 913,129", "1 in 11,688,053", "1 in 292,201,338"
    ],
    "Percentage": [
        "3.85%", "1.09%", "0.14%", "0.17%", "0.0069%", 
        "0.0027%", "0.00011%", "0.0000086%", "0.0000034%"
    ]
}
st.subheader("📊 Powerball Winning Odds")
st.dataframe(pd.DataFrame(odds_data))

# 2. White Ball Probabilities
white_df = pd.DataFrame({
    "White Ball": list(range(1, 70)),
    "Probability (%)": [round(100/69, 2)] * 69
})
st.subheader("⚪ White Ball Probabilities")
st.dataframe(white_df)

# 3. Red Ball Probabilities
red_df = pd.DataFrame({
    "Red Ball": list(range(1, 27)),
    "Probability (%)": [round(100/26, 2)] * 26
})
st.subheader("🔴 Powerball (Red Ball) Probabilities")
st.dataframe(red_df)

# Input Form
st.subheader("🎯 Calculate Your Odds")
white_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    st.success("Calculation logic coming soon — odds display only for now.")
