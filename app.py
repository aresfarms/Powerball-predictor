
import streamlit as st
import pandas as pd
import random

st.set_page_config(layout="wide", page_title="Powerball Predictor")

st.title("🎯 Powerball Predictor App")
st.markdown("Enter your number picks and calculate your odds of winning. Now with **friendly odds and payout summaries**!")

# --- User Inputs ---
with st.sidebar:
    st.header("Pick Your Numbers")
    white_balls = [st.number_input(f"White Ball #{i+1}", min_value=1, max_value=69, step=1) for i in range(5)]
    powerball = st.number_input("Powerball", min_value=1, max_value=26, step=1)
    st.markdown("---")
    calculate = st.button("Calculate Odds")

# --- Winning Odds Table ---
def display_odds_table():
    data = {
        "Match Type": [
            "Match Powerball only",
            "Match 1 white ball + Powerball",
            "Match 2 white balls + Powerball",
            "Match 3 white balls",
            "Match 3 white balls + Powerball",
            "Match 4 white balls",
            "Match 4 white balls + Powerball",
            "Match 5 white balls only",
            "Match 5 white balls + Powerball (Jackpot)"
        ],
        "Prize": [
            "$4", "$4", "$7", "$7", "$100", "$100", "$50,000", "$1 million", "Jackpot"
        ],
        "Odds": [
            "1 in 26", "1 in 92", "1 in 701", "1 in 579", "1 in 14,494",
            "1 in 36,525", "1 in 913,129", "1 in 11,688,053", "1 in 292,201,338"
        ],
        "Percentage": [
            "3.85%", "1.09%", "0.14%", "0.17%", "0.0069%", "0.0027%",
            "0.00011%", "0.0000086%", "0.00000034%"
        ]
    }
    df = pd.DataFrame(data)
    st.markdown("### 📊 Powerball Odds & Payout Summary")
    st.dataframe(df, use_container_width=True)

# --- Odds Calculator ---
def calculate_combination_odds():
    if set(white_balls) == set(range(1, 6)) and powerball == 1:
        return "🎉 Jackpot Winner! (1 in 292,201,338)", "Basically 0% (you won’t win)"
    else:
        return "Not a winning combination", "Virtually 0%"

if calculate:
    odds_result, chance_percent = calculate_combination_odds()
    st.markdown(f"## 🎲 Results")
    st.write(f"**Your odds of hitting the jackpot:** {odds_result}")
    st.write(f"**Winning Chance:** {chance_percent}")

# Show the odds table
display_odds_table()
