import webbrowser
import time

def open_rocket_league_tracker():
    url = "https://rocketleague.tracker.network/rocket-league/profile/steam/7656119922990327320/overview"
    webbrowser.open(url)

while True:
    open_rocket_league_tracker()
    time.sleep(900)  # Sleep for 15 minutes (900 seconds)
