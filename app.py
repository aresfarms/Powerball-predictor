
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chaos-Based Powerball Predictor", layout="centered")

st.title("Chaos-Based Powerball Predictor")
st.markdown("**(Friendly Odds)**")

white_balls_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

def calculate_odds(white_balls, powerball):
    if len(set(white_balls)) != 5 or any((n < 1 or n > 69) for n in white_balls) or powerball < 1 or powerball > 26:
        return None

    match_counts = [(5, True), (5, False), (4, True), (4, False),
                    (3, True), (3, False), (2, True),
                    (1, True), (0, True)]
    prize_values = ["Jackpot", "$1,000,000", "$50,000", "$100",
                    "$100", "$7", "$7", "$4", "$4"]
    odds_values = [292201338, 11688053.52, 913129.18, 36525.17,
                   14494.11, 579.76, 701.33, 91.98, 38.32]

    results = []
    for (match, pb), prize, odds in zip(match_counts, prize_values, odds_values):
        inverse_odds = 1 / odds
        if odds > 1_000_000:
            friendly = "Virtually zero chance"
        elif inverse_odds > 0.5:
            friendly = f"More likely than not ({round(inverse_odds*100, 2)}%)"
        else:
            friendly = f"1 in {int(odds):,} ({round(inverse_odds*100, 5)}%)"
        results.append({
            "White Balls Matched": match,
            "Powerball Matched": "Yes" if pb else "No",
            "Prize": prize,
            "Odds": friendly
        })

    return pd.DataFrame(results)

if st.button("Calculate Winning Odds"):
    try:
        white_balls = list(map(int, white_balls_input.strip().split(",")))
        df = calculate_odds(white_balls, powerball_input)
        if df is not None:
            st.dataframe(df)
        else:
            st.error("Invalid input: Please enter exactly 5 unique white ball numbers between 1 and 69.")
    except:
        st.error("Invalid input: Please enter comma-separated numbers like 5,12,23,34,55")
