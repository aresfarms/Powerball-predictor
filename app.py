
import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Chaos-Based Powerball Predictor", layout="centered")

st.title("Chaos-Based Powerball Predictor")
st.subheader("(Friendly Odds)")

white_balls_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    try:
        white_balls = [int(n.strip()) for n in white_balls_input.split(",")]
        if len(white_balls) != 5 or not all(1 <= n <= 69 for n in white_balls):
            st.error("Please enter exactly 5 white balls between 1 and 69.")
        else:
            total_combinations = math.comb(69, 5) * 26
            match_combo = 1
            odds = match_combo / total_combinations
            percent = odds * 100

            if percent > 90:
                summary = f"Jackpot Odds: {percent:.2f}% — Almost certain win"
            elif percent > 50:
                summary = f"Jackpot Odds: {percent:.2f}% — Very high chance of winning"
            elif percent > 0.01:
                summary = f"Jackpot Odds: {percent:.4f}%"
            else:
                summary = "Jackpot Odds: Virtually zero — not a winning combination"

            st.success(summary)

            data = {
                "Match Type": [
                    "5 White Balls + Powerball",
                    "5 White Balls",
                    "4 White Balls + Powerball",
                    "4 White Balls",
                    "3 White Balls + Powerball",
                    "3 White Balls",
                    "2 White Balls + Powerball",
                    "1 White Ball + Powerball",
                    "Powerball Only"
                ],
                "Odds (1 in ...)": [
                    "292,201,338",
                    "11,688,053",
                    "913,129",
                    "36,525",
                    "14,494",
                    "579",
                    "701",
                    "91",
                    "38"
                ],
                "Probability (%)": [
                    "0.00000034%", "0.0000086%", "0.00011%", "0.0027%",
                    "0.0069%", "0.17%", "0.14%", "1.10%", "2.63%"
                ]
            }
            st.markdown("### Powerball Match Probabilities")
            st.table(pd.DataFrame(data))

            red_ball_data = pd.DataFrame({
                "Powerball Match Count": [0, 1],
                "Odds (1 in ...)": ["1.38", "25.92"],
                "Probability (%)": ["72.0%", "3.85%"]
            })

            white_ball_data = pd.DataFrame({
                "White Ball Match Count": list(range(0, 6)),
                "Odds (1 in ...)": ["1.37", "1.64", "2.71", "7.2", "91", "292,201,338"],
                "Probability (%)": ["72.9%", "61.0%", "36.9%", "13.9%", "1.1%", "0.00000034%"]
            })

            st.markdown("### Red Ball (Powerball) Match Breakdown")
            st.table(red_ball_data)

            st.markdown("### White Ball Match Breakdown")
            st.table(white_ball_data)

    except Exception as e:
        st.error(f"Error: {e}")
