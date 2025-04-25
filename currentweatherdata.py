import requests
import pandas as pd
import logging
from datetime import datetime
from json import JSONDecodeError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger("weather_pipeline")

# Enter your API key here
api_key = "2bfefc746a8da258bca71e7114c696a6"

def get_current_weather(city, api_key):
    """Fetch current weather data for a specific city."""
    # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" # Use metric units (Celsius)
        }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # Raise exception for 4XX/5XX responses
        data = response.json()

        # Extract relevant data
        weather = data["weather"][0]
        main = data["main"]
        wind = data["wind"]
        ts = data["dt"]
        
        weather_data =  {
            "city": city,
            "time_creation": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "time_calculation": datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
            "temp": main["temp"],
            "humidity": main["humidity"],
            "wind_speed": wind["speed"],
            "condition": weather["main"],
            "description": weather["description"],
            # "icon": weather["icon"] # TODO: get icon (https://openweathermap.org/weather-conditions)
        }
        
        logger.info(f"Successfully fetched current weather data for {city}")
        return weather_data

    except requests.exceptions.Timeout as err:
        logger.error(f"Timeout fetching weather for {city}: {err}")
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP {response.status_code} for {city}: {err}")
    except requests.exceptions.RequestException as err:
        logger.error(f"Network error for {city}: {err}")
    except JSONDecodeError as err:
        logger.error(f"Invalid JSON for {city}: {err}")
    except (KeyError, TypeError) as err:
        logger.error(f"Unexpected data format for {city}: {err}")

    return None

data = get_current_weather(city='Kigali', api_key=api_key)

pd.DataFrame([data]) # why we add []: https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe

print(data)