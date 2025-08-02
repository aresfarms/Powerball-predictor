import requests
from bs4 import BeautifulSoup

def get_latest_numbers():
    url = "https://www.powerball.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    balls = soup.select(".numbers li")
    numbers = [int(ball.get_text()) for ball in balls if ball.get_text().isdigit()]
    return numbers[:5] + [numbers[-1]]
