from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def fetch_weather():
    api_url = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/159880/period/latest-hour/data.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "weather-app",
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        temperature = data["value"][0]["value"]
        return f"Current temperature: {temperature}°C"
    else:
        return "Failed to fetch data from SMHI API", response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
