def calculate_odds(user_input, latest_draw):
    try:
        user_numbers = list(map(int, user_input.split(',')))
        match_count = sum(1 for n in user_numbers if n in latest_draw)
        odds = "1 in 292,201,338 (virtually zero)" if match_count < 3 else "Significant chance"
        result = "Winner!" if match_count >= 5 else "Not a winner"
        return odds, result
    except:
        return "Invalid input", "Error"

def display_tables():
    import streamlit as st
    st.subheader("Probability Table")
    st.write("Match Powerball only ($4): 1 in 26 chance (3.85%)")
    st.write("Match 1 white ball + Powerball ($4): 1 in 92 chance (1.09%)")
    st.write("... and so on ...")
