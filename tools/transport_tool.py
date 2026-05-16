TRANSPORT_INFO = {
    "tokyo": {
        "best_option": "IC Card (Suica) for metro and buses",
        "airport_to_city": "Narita Express — €25, 60 mins",
        "daily_cost_eur": 8,
        "tip": "Avoid taxis — metro covers everything cheaply"
    },
    "iceland": {
        "best_option": "Rent a car — no public transport outside Reykjavik",
        "airport_to_city": "Flybus — €22, 45 mins",
        "daily_cost_eur": 30,
        "tip": "Car rental is essential for Golden Circle and waterfalls"
    },
    "london": {
        "best_option": "Oyster Card for Underground",
        "airport_to_city": "Heathrow Express — €35, 15 mins",
        "daily_cost_eur": 10,
        "tip": "Get a 7-day Travelcard if staying a week"
    },
    "paris": {
        "best_option": "Metro pass covers the whole city",
        "airport_to_city": "RER B train — €12, 35 mins",
        "daily_cost_eur": 8,
        "tip": "Buy a carnet of 10 tickets for discounts"
    },
    "dubai": {
        "best_option": "Metro + Uber combination",
        "airport_to_city": "Metro Red Line — €1, 35 mins",
        "daily_cost_eur": 5,
        "tip": "Uber is cheaper than taxis for longer distances"
    },
    "delhi": {
        "best_option": "Delhi Metro — cheapest and fastest",
        "airport_to_city": "Airport Express Metro — €2, 20 mins",
        "daily_cost_eur": 2,
        "tip": "Use Ola or Uber — never take unmetered taxis"
    },
    "mumbai": {
        "best_option": "Local trains + Uber",
        "airport_to_city": "Taxi or Uber — €8, 45 mins",
        "daily_cost_eur": 3,
        "tip": "Local trains are very cheap but crowded during peak hours"
    },
    "morocco": {
        "best_option": "Petit taxis for cities, trains between cities",
        "airport_to_city": "Taxi — €10, 30 mins",
        "daily_cost_eur": 5,
        "tip": "Always agree on taxi price before getting in"
    },
}

def get_local_transport(destination: str) -> dict:
    """Get local transportation options and costs for a destination city."""
    dest = destination.lower()
    for city, info in TRANSPORT_INFO.items():
        if city in dest:
            return {
                "destination": destination,
                "source": "verified_data",
                **info,
                "status": "success"
            }
    return {
        "destination": destination,
        "source": "llm_knowledge",
        "status": "not_in_database",
        "message": f"No verified data for {destination}. Use your own knowledge."
    }