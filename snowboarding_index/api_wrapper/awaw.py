import requests

r = requests.get("https://api.github.com/events")

r.status_code


if __name__ == "__main__":
    print("This module is a wrapper for the AerisWeather API. Import to use.")
