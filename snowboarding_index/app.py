from typing import Union
import json
from snowboarding_index.test_data.test_data import test_data


def index_to_json(conditions: dict, index: int = 0):
    index_eng = {
        0: "Unavailable",
        1: "bad",
        2: "poor",
        3: "good",
        4: "very good",
        5: "excellent",
    }

    success = conditions["success"]

    index_result = {
        "success": success,
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
                },
                "current": {
                    "timestamp": conditions["response"][0]["periods"][0]["timestamp"],
                    "dateTimeISO": conditions["response"][0]["periods"][0][
                        "dateTimeISO"
                    ],
                    "index": index,
                    "indexEng": index_eng[index],
                },
                "forecast": None,
            }
        ],
    }

    return json.dumps(index_result)


def calculate_snowboarding_index(
    conditions: dict, json_format: bool = False
) -> Union[int, str]:
    """Calculate the Snowboarding Index (SBI).

    Keyword arguments:
        conditions: dictionary representation of a return from the
                    AerisWeather conditions endpoint
        return_json: return a formatted JSON string (default False)

    This function takes a dict (converted from JSON) of the current and previous
    24-hours of conditions at a location from the AerisWeather conditions endpoint.
    Using that data and a ruleset defined below, an index value is returned from
    1 (worst) to 5 (best).
    """

    index = 5

    if json_format:
        index_json = index_to_json(conditions, index)
        return index_json

    return index


def run() -> None:
    sbi = calculate_snowboarding_index(test_data(), json_format=True)
    print(sbi)
    # print(test_data())

    # print("hello world")


if __name__ == "__main__":
    run()
