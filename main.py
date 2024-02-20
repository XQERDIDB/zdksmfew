import time
import webbrowser

# Initialize a counter
counter = 0

# Open the website initially
url = "https://rocketleague.tracker.network/rocket-league/profile/steam/7656119922990327320/overview"
webbrowser.open(url)
print('Opened')

while True:
  # Keep it open for 5 minutes
  time.sleep(300)  # 300 seconds = 5 minutes

  # Refresh the page (equivalent to closing and reopening)
  webbrowser.open(url)
  print("New tab opened")
  # Wait for 10 minutes before repeating
  time.sleep(600)  # 900 seconds = 10 minutes
  print("10 minutes passed")
  counter += 1
  print(f"Total tabs opened: {counter}")
