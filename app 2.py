
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos-Based Powerball Predictor", layout="centered")

st.title("Chaos-Based Powerball Predictor")
st.subheader("(Friendly Odds)")

white_balls = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

def calculate_odds():
    return [
        {"Match Type": "Match Powerball only", "Prize": "$4", "Odds": "1 in 26", "Percentage": "3.85%"},
        {"Match Type": "Match 1 white ball + Powerball", "Prize": "$4", "Odds": "1 in 92", "Percentage": "1.09%"},
        {"Match Type": "Match 2 white balls + Powerball", "Prize": "$7", "Odds": "1 in 701", "Percentage": "0.14%"},
        {"Match Type": "Match 3 white balls", "Prize": "$7", "Odds": "1 in 579", "Percentage": "0.17%"},
        {"Match Type": "Match 3 white + Powerball", "Prize": "$100", "Odds": "1 in 14,494", "Percentage": "0.0069%"},
        {"Match Type": "Match 4 white balls", "Prize": "$100", "Odds": "1 in 36,525", "Percentage": "0.0027%"},
        {"Match Type": "Match 4 white + Powerball", "Prize": "$50,000", "Odds": "1 in 913,129", "Percentage": "0.00011%"},
        {"Match Type": "Match 5 white balls only", "Prize": "$1 million", "Odds": "1 in 11,688,053", "Percentage": "0.0000086%"},
        {
            "Match Type": "Match 5 white + Powerball",
            "Prize": "Jackpot",
            "Odds": "1 in 292,201,338",
            "Percentage": "0.00000034%",
        },
    ]

def interpret_jackpot_odds():
    raw_odds = 1 / 292_201_338
    percentage = raw_odds * 100
    if percentage < 0.001:
        return "Virtually zero chance of winning"
    elif percentage > 50:
        return f"More likely than not: {percentage:.2f}% chance of winning"
    else:
        return f"Extremely unlikely ({percentage:.10f}%)"

if st.button("Calculate Winning Odds"):
    odds_table = calculate_odds()
    df = pd.DataFrame(odds_table)
    st.table(df)

    st.markdown("### National Powerball Jackpot Odds")
    st.markdown(interpret_jackpot_odds())
