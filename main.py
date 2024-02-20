import webbrowser
from jinja2 import escape
from threading import Timer
from flask import Flask

app = Flask(__name__)

# Your original code
def open_website():
    url = "https://rocketleague.tracker.network/rocket-league/profile/steam/7656119922990327320/overview"
    webbrowser.open(url)
    print("Opened")

# Route for the Flask app
@app.route("/")
def hello():
    return "Hello World!"

# Timer to open the website after 1 second
def open_browser():
    Timer(1, open_website).start()

if __name__ == "__main__":
    # Start the Flask app
    Timer(1, open_browser).start()
    app.run(port=2000)
