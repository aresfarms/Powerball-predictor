
import pandas as pd

def calculate_odds(white_balls, powerball):
    # Simulated logic for demonstration
    if white_balls == [1, 2, 3, 4, 5] and powerball == 1:
        return 0.75  # Simulate a 75% win chance for demo
    return 0.0000000034  # Realistic low odds

def get_friendly_odds(user_odds, jackpot_odds):
    if user_odds >= 0.5:
        return f"{round(user_odds * 100)}% chance of winning (more likely than not)"
    elif user_odds < 1e-6:
        return "Basically zero chance of winning"
    else:
        return f"1 in {round(1/user_odds):,} ({round(user_odds * 100, 6)}%)"

def generate_tables(white_balls, powerball):
    table1 = pd.DataFrame({
        "Matched Balls": ["5 + Powerball", "5", "4 + Powerball", "4"],
        "Estimated Payout": ["Jackpot", "$1,000,000", "$50,000", "$100"],
        "Odds": ["1 in 292,201,338", "1 in 11,688,053", "1 in 913,129", "1 in 36,525"]
    })
    table2 = pd.DataFrame({
        "Matched Balls": ["3 + Powerball", "3", "2 + Powerball", "1 + Powerball", "Powerball Only"],
        "Estimated Payout": ["$100", "$7", "$7", "$4", "$4"],
        "Odds": ["1 in 14,494", "1 in 579", "1 in 701", "1 in 92", "1 in 38"]
    })
    return [table1, table2]
