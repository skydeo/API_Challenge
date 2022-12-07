import json

from snowboarding_index.data_structures.period_data_frame import PeriodDataFrame


def json_to_pdf(conditions: dict) -> PeriodDataFrame:
    """Convert a JSON period record from the AerisWeather API into
    a PeriodDataFrame populated with the relevant values.
    """

    data_types = conditions.keys()

    snowIN = conditions["snowIN"] if "snowIN" in data_types else 0
    snowRateIN = conditions["snowRateIN"] if "snowRateIN" in data_types else 0
    tempC = conditions["tempC"] if "tempC" in data_types else 100
    feelslikeC = conditions["feelslikeC"] if "feelslikeC" in data_types else 100
    windSpeedMPH = conditions["windSpeedMPH"] if "windSpeedMPH" in data_types else 100

    pdf = PeriodDataFrame(
        snowIN=snowIN,
        snowRateIN=snowRateIN,
        tempC=tempC,
        feelslikeC=feelslikeC,
        windSpeedMPH=windSpeedMPH,
    )

    return pdf


def index_to_json(conditions: dict, index: int, index_eng: str):
    """Given an index value and english rating equivalent, output a JSON
    string that matches other AerisWeather Index API output.
    """
    index_json = {
        "success": conditions["success"],
        "error": conditions["error"],
        "response": [
            {
                "loc": {
                    "lat": conditions["response"][0]["loc"]["lat"],
                    "long": conditions["response"][0]["loc"]["long"],
                },
                "indice": {
                    "type": "snowboarding",
                    "range": {
                        "min": 1,
                        "max": 5,
                        "reverse": False,
                    },
                    "past": None,
                    "current": {
                        "timestamp": conditions["response"][0]["periods"][0][
                            "timestamp"
                        ],
                        "dateTimeISO": conditions["response"][0]["periods"][0][
                            "dateTimeISO"
                        ],
                        "index": index,
                        "indexEng": index_eng,
                    },
                    "forecast": None,
                },
                "place": {
                    "name": conditions["response"][0]["place"]["name"],
                    "state": conditions["response"][0]["place"]["state"],
                    "country": conditions["response"][0]["place"]["country"],
                },
                "profile": {"tz": conditions["response"][0]["profile"]["tz"]},
            }
        ],
    }

    return json.dumps(index_json)
