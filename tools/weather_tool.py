import requests

def get_weather(city: str) -> dict:
    """Get real current weather for a city using wttr.in free API."""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        data = response.json()
        current = data["current_condition"][0]
        return {
            "city": city,
            "temperature_c": current["temp_C"],
            "feels_like_c": current["FeelsLikeC"],
            "condition": current["weatherDesc"][0]["value"],
            "humidity_pct": current["humidity"],
            "wind_kmph": current["windspeedKmph"],
            "status": "success"
        }
    except Exception as e:
        return {"city": city, "status": "error", "message": str(e)}