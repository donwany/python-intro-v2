# Real-World Example: API Request (Weather App)
import requests


def weather(city):
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": "YOUR_API_KEY"},
            timeout=5
        )
        response.raise_for_status()  # Raises HTTPError if bad response
        return response.json()
    except ValueError as e:
        print("Configuration Error:", e)
    except KeyError as e:
        print(f"Unexpected response format: {e}")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.HTTPError:
        print("City not found or API error.")
    except requests.exceptions.RequestException:
        print("Network error occurred.")

    return None
