from dataclasses import dataclass


@dataclass
class PeriodDataFrame:
    """Class for keeping track of SBI relevant data and functions. Stores the relevant
    data values, includes functions to score these based on rules and weights, and
    return a sum weighted index value.

    Weighting:
        snowIN: 4
        snowRateIN: 1
        tempC: 2
        feelslikeC: 1
        windSpeedMPH: 2

    Scoring:
        snowIN:         proportional scale from min 0.1 up to max of 0.5in/hr
        snowRateIN:     proportional scale frommin 0.05  to max of 0.1in/hr
        tempC:          binary, must be below freezing
        feelslikeC:     scales down from target value (2C)to +/- range (12C) on both sides of target
        windSpeedMPH:   inverse scale from min 0mph to max 20mph
    """

    snowIN: float
    snowRateIN: float
    tempC: float
    feelslikeC: float
    windSpeedMPH: float

    weights = {
        "snowIN": 2,
        "snowRateIN": 0.5,
        "tempC": 1,
        "feelslikeC": 0.5,
        "windSpeedMPH": 1,
    }

    rules = {
        "snowIN": {"min": 0.1, "max": 0.5},
        "snowRateIN": {"min": 0.05, "max": 0.1},
        "tempC": {"max": 0},
        "feelslikeC": {"target": 2, "range": 12},
        "windSpeedMPH": {"target": 0, "upper_bound": 20},
    }

    def score_snowIN(self) -> float:
        if self.snowIN < self.rules["snowIN"]["min"]:
            score = 0
        elif self.snowIN >= self.rules["snowIN"]["max"]:
            score = 1
        else:
            score = (self.snowIN - self.rules["snowIN"]["min"]) / (
                self.rules["snowIN"]["max"] - self.rules["snowIN"]["min"]
            )
        return score * self.weights["snowIN"]

    def score_snowRateIN(self) -> float:
        if self.snowRateIN < self.rules["snowRateIN"]["min"]:
            score = 0
        elif self.snowRateIN >= self.rules["snowRateIN"]["max"]:
            score = 1
        else:
            score = (self.snowRateIN - self.rules["snowRateIN"]["min"]) / (
                self.rules["snowRateIN"]["max"] - self.rules["snowRateIN"]["min"]
            )
        return score * self.weights["snowRateIN"]

    def score_tempC(self) -> int:
        if self.tempC > self.rules["tempC"]["max"]:
            score = 0
        else:
            score = 1
        return score * self.weights["tempC"]

    def score_feelslikeC(self) -> float:
        target = self.rules["feelslikeC"]["target"]
        range = self.rules["feelslikeC"]["range"]
        rangeMax = target + range
        rangeMin = target - range
        if (self.feelslikeC > rangeMax) or (self.feelslikeC < rangeMin):
            score = 0
        else:
            score = 1 - (abs(target - self.feelslikeC) / range)
        return score * self.weights["feelslikeC"]

    def score_windSpeedMPH(self) -> float:
        if self.windSpeedMPH > self.rules["windSpeedMPH"]["upper_bound"]:
            score = 0
        else:
            score = 1 - (self.windSpeedMPH / self.rules["windSpeedMPH"]["upper_bound"])
        return score * self.weights["windSpeedMPH"]

    def calculate_sbi_score(self) -> float:
        component_scores = [
            self.score_snowIN(),
            self.score_snowRateIN(),
            self.score_tempC(),
            self.score_feelslikeC(),
            self.score_windSpeedMPH(),
        ]

        return sum(component_scores)
