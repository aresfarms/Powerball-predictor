
import streamlit as st
import pandas as pd

st.title("Powerball Predictor - Static Demo")

# Sample user input
user_white_balls = st.multiselect("Pick 5 White Balls", list(range(1, 70)), default=[10, 20, 30, 40, 50])
user_red_ball = st.selectbox("Pick 1 Powerball", list(range(1, 27)), index=10)

# Odds table
odds_data = {
    "Match": [
        "Powerball only ($4)",
        "1 white + Powerball ($4)",
        "2 white + Powerball ($7)",
        "3 white ($7)",
        "3 white + Powerball ($100)",
        "4 white ($100)",
        "4 white + Powerball ($50,000)",
        "5 white ($1 million)",
        "5 white + Powerball (Jackpot)"
    ],
    "Odds (1 in X)": [
        "26", "92", "701", "579", "14,494", "36,525", "913,129", "11,688,053", "292,201,338"
    ],
    "Percent Chance": [
        "3.85%", "1.09%", "0.14%", "0.17%", "0.0069%", "0.0027%", "0.00011%", "0.0000086%", "0.00000034%"
    ]
}

df = pd.DataFrame(odds_data)
st.subheader("Powerball Odds Table")
st.dataframe(df)

# Static check
st.subheader("Results:")
if set(user_white_balls) == {10, 20, 30, 40, 50} and user_red_ball == 11:
    st.success("🎉 This is the winning combination!")
else:
    st.warning("❌ Not a winning combination.")
