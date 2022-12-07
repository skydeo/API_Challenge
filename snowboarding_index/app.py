import argparse
from typing import NamedTuple

from snowboarding_index.awaw.awaw import fetch_conditions
from snowboarding_index.transform_data.converters import index_to_json, json_to_pdf


def calculate_weighted_sbi(hourly_sbi_values: list[float]) -> float:
    weights = sorted(range(1, len(hourly_sbi_values) + 1), reverse=True)
    weighted_scores = [a * b for a, b in zip(hourly_sbi_values, weights)]
    weighted_sbi = sum(weighted_scores) / sum(weights)
    return weighted_sbi


def fudge_sbi_score(weighted_sbi: float, fudge_factor: float) -> float:
    fudged_sbi = min(weighted_sbi * fudge_factor, 5)
    return fudged_sbi


def beautify_name(place: dict) -> str:
    place_name = (
        place["name"].title()
        + ", "
        + place["state"].upper()
        + ", "
        + place["country"].upper()
    )
    return place_name


def index_to_eng(index: int) -> str:
    index_eng = {
        0: "Unavailable",
        1: "bad",
        2: "poor",
        3: "good",
        4: "very good",
        5: "excellent",
    }

    return index_eng[index]


def calculate_snowboarding_index(
    conditions: dict, json_format: bool = False, fudge_sbi: bool = True
) -> NamedTuple:
    """Calculate the Snowboarding Index (SBI).

    Keyword parameter:
        conditions: dictionary representation of a return from the
                    AerisWeather conditions endpoint.
    Optional parameter:
        return_json: (default False) return a JSON string formatted
                     to match the AerisWeather Index API
        fudge_sbi: fudge the sbi value to more closely match other indices

    This function takes a dict (converted from JSON) of the current (and optionally
    future hours) of conditions at a location from the AerisWeather conditions endpoint.
    Using that data and a ruleset defined in the PeriodDataFrame class, an index value
    is returned from 1 (worst) to 5 (best).
    """

    SBI_Index = NamedTuple("SBI", [("index", int), ("index_eng", str)])

    try:
        periods = conditions["response"][0]["periods"]
    except KeyError:
        index = 0
        return SBI_Index(index, index_to_eng(sbi))

    pdfs = [json_to_pdf(period) for period in periods]

    hourly_sbi_values = [pdf.calculate_sbi_score() for pdf in pdfs]
    weighted_sbi = calculate_weighted_sbi(hourly_sbi_values)
    if fudge_sbi:
        weighted_sbi = fudge_sbi_score(weighted_sbi, 1.5)

    sbi = round(weighted_sbi)

    if json_format:
        try:
            formatted_json = index_to_json(conditions, sbi, index_to_eng(sbi))
        except KeyError:
            index = 0
            return SBI_Index(index, index_to_eng(sbi))
        return formatted_json

    index = SBI_Index(sbi, index_to_eng(sbi))

    return index


def run() -> None:
    parser = argparse.ArgumentParser(
        prog="SBI Calculator",
        description="Calculate the Snowboarding Index (SBI) for a location.",
    )
    parser.add_argument(
        "-l",
        "--location",
        help="Location to find SBI. Enter a ZIP code or human-readable location (e.g., Minneapolis, MN)",
    )
    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="Display SBI in a JSON format matching the AerisWeather Index endpoint.",
    )
    parser.add_argument(
        "-ff",
        "--fudge_factor",
        action="store_false",
        help="Don't fudge the SBI to more closely match the AerisWeather Index endpoint.",
    )

    args = parser.parse_args()

    location = args.location
    return_json = args.json
    fudge_sbi = args.fudge_factor

    conditions = fetch_conditions(location=location, num_hours=8)

    place_name = beautify_name(conditions["response"][0]["place"])

    sbi = calculate_snowboarding_index(
        conditions, json_format=return_json, fudge_sbi=fudge_sbi
    )

    if return_json:
        print(sbi)
    else:
        print(
            f"The snowboarding index for \033[1m{place_name}\033[0m is: {sbi.index} ({sbi.index_eng})"
        )


if __name__ == "__main__":
    run()
