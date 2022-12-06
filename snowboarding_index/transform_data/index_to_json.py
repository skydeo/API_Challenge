import json


def index_to_json(conditions: dict, index: int, index_eng: str):
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
