from collections import namedtuple
from typing import Union

from snowboarding_index.test_data.test_data import test_data
from snowboarding_index.transform_data.index_to_json import index_to_json


def evaluate_conditions(conditions: dict) -> int:
    """Takes in the conditions for a given time period (from the AerisWeather API),
    and converts it to an index value based on the ruleset below. The different
    parameters have different weights and scoring conditions depending on data
    type.

    Weighting:
        snowIN: 4
        tempC: 2
        feelslikeC: 1
        windSpeedMPH: 2
        snowRateIN: 1

    Scoring:
        snowIN: proportional scale from min 0.1 up to max of 0.5in/hr
        snowRateIN: proportional scale frommin 0.05  to max of 0.1in/hr
        tempC: binary, must be below freezing
        feelslikeC: scales down from target value to +/- range on both sides of target
        windSpeedMPH: inverse scale from min 0mph to max 20mph
    """

    weights = {
        "snowIN": 2,
        "snowRateIN": 0.5,
        "tempC": 1,
        "feelslikeC": 0.5,
        "windSpeedMPH": 1,
    }

    rules = {
        "snowIN": {"min": 0.1, "max": 0.3},
        "snowRateIN": {"min": 0.01, "max": 0.05},
        "tempC": {"max": 0},
        "feelslikeC": {"target": 2, "range": 14},
        "windSpeedMPH": {"target": 0, "upper_bound": 20},
    }

    index = 0

    keys = conditions.keys()

    if "snowIN" in keys:
        snowIN = conditions["snowIN"]
        if snowIN < rules["snowIN"]["min"]:
            score = 0
        elif snowIN > rules["snowIN"]["max"]:
            score = 1
        else:
            score = snowIN / (rules["snowIN"]["max"] - rules["snowIN"]["min"])
        weighted_score = score * weights["snowIN"]
        index += weighted_score

    if "snowRateIN" in keys:
        snowRateIN = conditions["snowRateIN"]
        if snowRateIN < rules["snowRateIN"]["min"]:
            score = 0
        elif snowRateIN >= rules["snowRateIN"]["max"]:
            score = 1
        else:
            score = snowRateIN / (
                rules["snowRateIN"]["max"] - rules["snowRateIN"]["min"]
            )
        weighted_score = score * weights["snowRateIN"]
        index += weighted_score

    if "tempC" in keys:
        tempC = conditions["tempC"]
        if tempC > rules["tempC"]["max"]:
            score = 0
        else:
            score = 1
        weighted_score = score * weights["tempC"]
        index += weighted_score

    if "feelslikeC" in keys:
        feelslikeC = conditions["feelslikeC"]
        target = rules["feelslikeC"]["target"]
        range = rules["feelslikeC"]["range"]
        rangeMax = target + range
        rangeMin = target - range
        if (feelslikeC > rangeMax) or (feelslikeC < rangeMin):
            score = 0
        else:
            score = 1 - (abs(target - feelslikeC) / range)
        weighted_score = score * weights["feelslikeC"]
        index += weighted_score

    if "windSpeedMPH" in keys:
        windSpeedMPH = conditions["windSpeedMPH"]
        if windSpeedMPH > rules["windSpeedMPH"]["upper_bound"]:
            score = 0
        else:
            score = 1 - (windSpeedMPH / rules["windSpeedMPH"]["upper_bound"])
        weighted_score = score * weights["windSpeedMPH"]
        index += weighted_score

    return index


def calculate_snowboarding_index(
    conditions: dict, json_format: bool = False
) -> Union[int, str]:
    """Calculate the Snowboarding Index (SBI).

    Keyword arguments:
        conditions: dictionary representation of a return from the
                    AerisWeather conditions endpoint
        return_json: return a formatted JSON string (default False)

    This function takes a dict (converted from JSON) of the current and future
    12 hours of conditions at a location from the AerisWeather conditions endpoint.
    Using that data and a ruleset defined in evaluate_conditions(), an index value
    is returned from 1 (worst) to 5 (best).
    """

    SBI_Index = namedtuple("SBI", ["index", "index_eng"])

    try:
        periods = conditions["response"][0]["periods"]
    except KeyError:
        index = 0
        return SBI_Index(index, index_eng[index])

    # Calculate the weighted sbi per period by
    #   1) Calculating the sbi for each period
    #   2) Creating a weight list, with weights proportionally decreasing/period
    #   3) Multiply the hourly indices by the corresponding weight
    hourly_index_values = [evaluate_conditions(period) for period in periods]
    weights = sorted(range(1, len(hourly_index_values) + 1), reverse=True)
    weighted_scores = [a * b for a, b in zip(hourly_index_values, weights)]

    # index = int(sum(weighted_scores) / sum(weights))
    # Added a fudge factor as a cheat to properly weighting different sbi parameters
    fudge_factor = 1.5
    index = sum(weighted_scores) / sum(weights)
    index = min(index * fudge_factor, 5)
    index = int(index)

    index_eng = {
        0: "Unavailable",
        1: "bad",
        2: "poor",
        3: "good",
        4: "very good",
        5: "excellent",
    }

    if json_format:
        return index_to_json(conditions, index, index_eng[index])

    sbi = SBI_Index(index, index_eng[index])

    return sbi


def run() -> None:
    return_json = False
    sbi = calculate_snowboarding_index(test_data(), json_format=return_json)
    if return_json:
        print(sbi)
    else:
        print(
            f"The snowboarding index for your location is: {sbi.index} ({sbi.index_eng})"
        )


if __name__ == "__main__":
    run()
