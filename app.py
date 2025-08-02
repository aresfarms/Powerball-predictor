import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos-Based Powerball Predictor", layout="centered")
st.title("Chaos-Based Powerball Predictor")
st.markdown("**(Friendly Odds)**")

white_balls_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

def calculate_odds(white_balls, powerball):
    if len(set(white_balls)) != 5 or any((n < 1 or n > 69) for n in white_balls) or powerball < 1 or powerball > 26:
        return None, None, None

    odds_table = []
    match_counts = [(5, True), (5, False), (4, True), (4, False), (3, True), (3, False), (2, True),
                    (1, True), (0, True), (3, False), (2, False), (1, False), (0, False)]
    prize_values = ["Jackpot", "$1,000,000", "$50,000", "$100", "$100", "$7", "$7",
                    "$4", "$4", "$7", "$4", "$0", "$0"]
    odds_values = [292201338, 11688053.52, 913129.18, 36525.17, 14494.11, 579.76, 701.33,
                   91.98, 38.32, 701.33, 579.76, 91.98, 38.32]

    for (match, pb), prize, odds in zip(match_counts, prize_values, odds_values):
        friendly = f"1 in {int(odds):,} ({round(1/odds*100, 8)}%)"
        if round(1/odds*100, 8) < 0.000001:
            friendly = "Virtually zero (not a winning combo)"
        elif round(1/odds*100, 8) >= 99:
            friendly = f"Highly Likely ({round(1/odds*100, 2)}%)"
        odds_table.append({
            "White Balls Matched": match,
            "Powerball Matched": "Yes" if pb else "No",
            "Prize": prize,
            "Odds": friendly
        })
    return odds_table

if st.button("Calculate Winning Odds"):
    try:
        white_balls = list(map(int, white_balls_input.split(",")))
        odds_table = calculate_odds(white_balls, powerball_input)
        if odds_table:
            df = pd.DataFrame(odds_table)
            st.markdown("### Winning Odds Breakdown")
            st.dataframe(df, use_container_width=True)
        else:
            st.error("Invalid input. Please enter 5 unique white balls between 1 and 69.")
    except:
        st.error("Invalid input format. Please enter 5 numbers separated by commas.")
