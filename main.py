import webbrowser
import time

# Initialize a counter
counter = 0

def open_rocket_league_tracker():
    global counter
    url = "https://rocketleague.tracker.network/rocket-league/profile/steam/7656119922990327320/overview"
    webbrowser.open(url)
    counter += 1

while True:
    # Open the website
    open_rocket_league_tracker()

    # Keep it open for 2 minutes
    time.sleep(120)  # 120 seconds = 2 minutes

    # Close the website
    webbrowser.open("about:blank")  # Opens a blank page, effectively closing the previous page

    # Wait for 15 minutes before repeating
    time.sleep(900)  # 900 seconds = 15 minutes

print(f"The website was opened and closed {counter} times.")
