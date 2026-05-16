import requests

FLIGHT_COSTS = {
    "tokyo": 650, "japan": 650,
    "iceland": 180, "reykjavik": 180,
    "new york": 400, "usa": 400,
    "london": 80, "paris": 70,
    "dubai": 300, "bangkok": 500,
    "singapore": 550, "sydney": 900,
    "rome": 100, "barcelona": 90,
    "delhi": 500, "india": 500,
    "mumbai": 500, "morocco": 250,
}

def get_flight_estimate(destination: str, duration_days: int) -> dict:
    """Estimate minimum travel budget from Germany to a destination in EUR."""
    dest = destination.lower()
    flight = next((v for k, v in FLIGHT_COSTS.items() if k in dest), 350)
    hotel      = 70 * duration_days
    food       = 30 * duration_days
    activities = 20 * duration_days
    total      = flight + hotel + food + activities

   

    return {
        "destination": destination,
        "duration_days": duration_days,
        "flight_eur": flight,
        "hotel_eur": hotel,
        "food_eur": food,
        "activities_eur": activities,
        "total_min_eur": total,
        "status": "success"
    }

def get_exchange_rate(amount_eur: float, target_currency: str) -> dict:
    """Convert EUR to another currency using live exchange rates."""
    try:
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
        rates = requests.get(url, timeout=5).json()["rates"]
        rate = rates.get(target_currency.upper(), 1.0)
        return {
            "amount_eur": amount_eur,
            "target_currency": target_currency.upper(),
            "converted_amount": round(amount_eur * rate, 2),
            "exchange_rate": rate,
            "status": "success"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}