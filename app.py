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
    match_counts = [(5, True), (5, False), (4, True), (4, False), (3, True), (3, False), (2, True), (1, True), (0, True)]
    prize_values = ["Jackpot", "$1,000,000", "$50,000", "$100", "$100", "$7", "$7", "$4", "$4"]
    odds_values = [292201338, 11688053.52, 913129.18, 36525.17, 14494.11, 579.76, 701.33, 91.98, 38.32]

    for (match, pb), prize, odds in zip(match_counts, prize_values, odds_values):
        friendly = f"1 in {int(odds):,} ({round(1/odds*100, 8)}%)"
        if int(odds) == 292201338:
            friendly += " – National Powerball Jackpot Odds: virtually zero chance of winning"
        odds_table.append({
            "White Balls Matched": match,
            "Powerball Matched": "Yes" if pb else "No",
            "Prize": prize,
            "Odds": friendly
        })

    # Match user input with match_counts
    matched_white = len(set(white_balls).intersection(set(user_draws)))
    matched_powerball = user_pb == powerball
    result = next((entry for entry in odds_table if entry["White Balls Matched"] == matched_white and
                   ((entry["Powerball Matched"] == "Yes") == matched_powerball)), None)

    return odds_table, result["White Balls Matched"] if result else None, result["Prize"] if result else None

if st.button("Calculate Winning Odds"):
    try:
        user_draws = [int(x.strip()) for x in white_balls_input.split(",") if x.strip().isdigit()]
        user_pb = int(powerball_input)

        odds_table, matched_white, prize = calculate_odds(user_draws, user_pb)

        if odds_table is not None:
            st.subheader("Odds Table")
            st.table(pd.DataFrame(odds_table))

            if prize == "Jackpot":
                st.success("🎉 Congratulations! You’ve hit the Jackpot (hypothetically)!")
            elif prize:
                st.info(f"🎯 You matched with prize: {prize}")
            else:
                st.warning("🚫 Not a winning combination. Basically zero chance of winning.")
        else:
            st.error("❗ Invalid numbers. Please enter 5 unique white balls from 1–69.")
    except Exception as e:
        st.error(f"❗ Error: {str(e)}")