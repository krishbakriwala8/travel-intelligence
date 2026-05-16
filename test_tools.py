from tools.weather_tool import get_weather
from tools.budget_tool  import get_flight_estimate, get_exchange_rate

# weather
print(get_weather("Tokyo"))

# budget
print(get_flight_estimate("Iceland", 10))

# currency
print(get_exchange_rate(1580, "ISK"))