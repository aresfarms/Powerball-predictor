
import streamlit as st
from utils import calculate_odds, get_friendly_odds, generate_tables

st.set_page_config(page_title="Chaos-Based Powerball Predictor", layout="centered")

st.markdown("# Chaos-Based Powerball Predictor")
st.markdown("### (Friendly Odds)")

white_balls_input = st.text_input("Enter 5 white balls (1–69) separated by commas")
powerball_input = st.number_input("Enter Powerball (1–26)", min_value=1, max_value=26, step=1)

if st.button("Calculate Winning Odds"):
    try:
        white_balls = list(map(int, white_balls_input.split(",")))
        if len(white_balls) != 5 or any(not (1 <= num <= 69) for num in white_balls):
            st.error("Please enter exactly 5 white balls, each between 1 and 69.")
        else:
            if not (1 <= powerball_input <= 26):
                st.error("Powerball must be between 1 and 26.")
            else:
                jackpot_odds = 1 / 292201338
                user_odds = calculate_odds(white_balls, powerball_input)
                friendly_odds = get_friendly_odds(user_odds, jackpot_odds)

                st.success(f"Your Odds of Hitting the Jackpot: {friendly_odds}")

                for table in generate_tables(white_balls, powerball_input):
                    st.dataframe(table)

    except ValueError:
        st.error("Invalid input. Please enter 5 numbers separated by commas.")
