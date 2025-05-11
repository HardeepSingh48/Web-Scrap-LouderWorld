from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper import scrape_events
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

event_cache = []
opt_in_list = []

def update_event_cache():
    global event_cache
    event_cache = scrape_events()
    print("Updated event cache")

scheduler = BackgroundScheduler()
scheduler.add_job(update_event_cache, 'interval', hours=1)
scheduler.start()

@app.route("/api/events")
def get_events():
    return jsonify(event_cache)

@app.route("/api/optin", methods=["POST"])
def opt_in():
    data = request.get_json()
    email = data.get("email")
    event_link = data.get("event_link")
    if not email or not event_link:
        return jsonify({"error": "Missing email or event_link"}), 400
    opt_in_list.append({"email": email, "event_link": event_link})
    print(f"New opt-in: {email} for event {event_link}")
    return jsonify({"message": "Opt-in received"}), 200

@app.route("/")
def index():
    return "Event Listing API is running."

if __name__ == "__main__":
    update_event_cache()
    app.run(debug=True)
