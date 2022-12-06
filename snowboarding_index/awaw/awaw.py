import requests
from dotenv import load_dotenv
import os


def fetch_conditions(location: str = None, num_hours: int = 1) -> dict:
    load_dotenv()

    if not location:
        location = ":auto"

    endpoint = "https://api.aerisapi.com/conditions/"
    params = {
        "format": "json",
        "to": f"+{num_hours}hours",
        "filter": "1hour",
        # "fields": "",
        # "plimit": 4,
        "client_id": os.environ["client_id"],
        "client_secret": os.environ["client_secret"],
    }

    url = endpoint + location

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

    try:
        conditions = r.json()
    except requests.exceptions.JSONDecodeError as err:
        raise SystemExit(err)

    if not conditions["success"]:
        err = conditions["error"]["description"]
        raise SystemError(err)

    return conditions


if __name__ == "__main__":
    print("This module is a wrapper for the AerisWeather API. Import to use.")
