import json

raw_data = """{
    "success": true,
    "error": null,
    "response": [
        {
            "loc": {
                "lat": 44.97997,
                "long": -93.26384
            },
            "place": {
                "name": "minneapolis",
                "state": "mn",
                "country": "us"
            },
            "periods": [
                {
                    "timestamp": 1670299200,
                    "dateTimeISO": "2022-12-05T22:00:00-06:00",
                    "tempC": -7.11,
                    "tempF": 19.2,
                    "feelslikeC": -9.64,
                    "feelslikeF": 14.65,
                    "dewpointC": -12.05,
                    "dewpointF": 10.31,
                    "humidity": 68,
                    "pressureMB": 1020,
                    "pressureIN": 30.12,
                    "windDir": "NNW",
                    "windDirDEG": 340,
                    "windSpeedKTS": 5,
                    "windSpeedKPH": 9.26,
                    "windSpeedMPH": 5.75,
                    "windGustKTS": 6,
                    "windGustKPH": 11.11,
                    "windGustMPH": 6.9,
                    "precipMM": 0,
                    "precipIN": 0,
                    "precipRateMM": 0,
                    "precipRateIN": 0,
                    "snowCM": 0,
                    "snowIN": 0,
                    "snowRateCM": 0,
                    "snowRateIN": 0,
                    "pop": 0,
                    "visibilityKM": 24.135,
                    "visibilityMI": 14.997,
                    "sky": 46,
                    "cloudsCoded": "SC",
                    "weather": "Partly Cloudy",
                    "weatherCoded": "::SC",
                    "weatherPrimary": "Partly Cloudy",
                    "weatherPrimaryCoded": "::SC",
                    "icon": "pcloudyn.png",
                    "solradWM2": 0,
                    "uvi": 0,
                    "isDay": false,
                    "spressureMB": 987.5,
                    "spressureIN": 29.16,
                    "altimeterMB": 1017.3,
                    "altimeterIN": 30.04,
                    "solrad": {
                        "azimuthDEG": 301.2777,
                        "zenithDEG": 146.0797,
                        "ghiWM2": 0,
                        "dniWM2": 0,
                        "dhiWM2": 0
                    }
                },
                {
                    "timestamp": 1670310000,
                    "dateTimeISO": "2022-12-06T01:00:00-06:00",
                    "tempC": -9.35,
                    "tempF": 15.17,
                    "feelslikeC": -9.35,
                    "feelslikeF": 15.17,
                    "dewpointC": -13.3,
                    "dewpointF": 8.06,
                    "humidity": 73,
                    "pressureMB": 1021,
                    "pressureIN": 30.15,
                    "windDir": "N",
                    "windDirDEG": 10,
                    "windSpeedKTS": 2,
                    "windSpeedKPH": 3.7,
                    "windSpeedMPH": 2.3,
                    "windGustKTS": 5,
                    "windGustKPH": 9.26,
                    "windGustMPH": 5.75,
                    "precipMM": 0,
                    "precipIN": 0,
                    "precipRateMM": 0,
                    "precipRateIN": 0,
                    "snowCM": 0,
                    "snowIN": 0,
                    "snowRateCM": 0,
                    "snowRateIN": 0,
                    "pop": 0,
                    "visibilityKM": 24.135,
                    "visibilityMI": 14.997,
                    "sky": 35,
                    "cloudsCoded": "SC",
                    "weather": "Partly Cloudy",
                    "weatherCoded": "::SC",
                    "weatherPrimary": "Partly Cloudy",
                    "weatherPrimaryCoded": "::SC",
                    "icon": "pcloudyn.png",
                    "solradWM2": 0,
                    "uvi": 0,
                    "isDay": false,
                    "spressureMB": 988.2,
                    "spressureIN": 29.18,
                    "altimeterMB": 1018,
                    "altimeterIN": 30.06,
                    "solrad": {
                        "azimuthDEG": 31.4252,
                        "zenithDEG": 154.7517,
                        "ghiWM2": 0,
                        "dniWM2": 0,
                        "dhiWM2": 0
                    }
                },
                {
                    "timestamp": 1670320800,
                    "dateTimeISO": "2022-12-06T04:00:00-06:00",
                    "tempC": -10.5,
                    "tempF": 13.1,
                    "feelslikeC": -10.5,
                    "feelslikeF": 13.1,
                    "dewpointC": -13.92,
                    "dewpointF": 6.94,
                    "humidity": 76,
                    "pressureMB": 1021,
                    "pressureIN": 30.15,
                    "windDir": "ENE",
                    "windDirDEG": 60,
                    "windSpeedKTS": 2,
                    "windSpeedKPH": 3.7,
                    "windSpeedMPH": 2.3,
                    "windGustKTS": 5,
                    "windGustKPH": 9.26,
                    "windGustMPH": 5.75,
                    "precipMM": 0,
                    "precipIN": 0,
                    "precipRateMM": 0,
                    "precipRateIN": 0,
                    "snowCM": 0,
                    "snowIN": 0,
                    "snowRateCM": 0,
                    "snowRateIN": 0,
                    "pop": 0,
                    "visibilityKM": 24.135,
                    "visibilityMI": 14.997,
                    "sky": 28,
                    "cloudsCoded": "FW",
                    "weather": "Mostly Clear",
                    "weatherCoded": "::FW",
                    "weatherPrimary": "Mostly Clear",
                    "weatherPrimaryCoded": "::FW",
                    "icon": "fairn.png",
                    "solradWM2": 0,
                    "uvi": 0,
                    "isDay": false,
                    "spressureMB": 988,
                    "spressureIN": 29.18,
                    "altimeterMB": 1017.9,
                    "altimeterIN": 30.06,
                    "solrad": {
                        "azimuthDEG": 85.1597,
                        "zenithDEG": 127.4195,
                        "ghiWM2": 0,
                        "dniWM2": 0,
                        "dhiWM2": 0
                    }
                },
                {
                    "timestamp": 1670331600,
                    "dateTimeISO": "2022-12-06T07:00:00-06:00",
                    "tempC": -10.55,
                    "tempF": 13.01,
                    "feelslikeC": -10.55,
                    "feelslikeF": 13.01,
                    "dewpointC": -13.8,
                    "dewpointF": 7.16,
                    "humidity": 77,
                    "pressureMB": 1021,
                    "pressureIN": 30.15,
                    "windDir": "ESE",
                    "windDirDEG": 110,
                    "windSpeedKTS": 2,
                    "windSpeedKPH": 3.7,
                    "windSpeedMPH": 2.3,
                    "windGustKTS": 8,
                    "windGustKPH": 14.82,
                    "windGustMPH": 9.21,
                    "precipMM": 0,
                    "precipIN": 0,
                    "precipRateMM": 0,
                    "precipRateIN": 0,
                    "snowCM": 0,
                    "snowIN": 0,
                    "snowRateCM": 0,
                    "snowRateIN": 0,
                    "pop": 0,
                    "visibilityKM": 24.135,
                    "visibilityMI": 14.997,
                    "sky": 31,
                    "cloudsCoded": "FW",
                    "weather": "Mostly Clear",
                    "weatherCoded": "::FW",
                    "weatherPrimary": "Mostly Clear",
                    "weatherPrimaryCoded": "::FW",
                    "icon": "fairn.png",
                    "solradWM2": 164,
                    "uvi": 0,
                    "isDay": false,
                    "spressureMB": 988,
                    "spressureIN": 29.18,
                    "altimeterMB": 1017.9,
                    "altimeterIN": 30.06,
                    "solrad": {
                        "azimuthDEG": 115.4745,
                        "zenithDEG": 96.505,
                        "ghiWM2": 163.551,
                        "dniWM2": 0,
                        "dhiWM2": 163.551
                    }
                },
                {
                    "timestamp": 1670342400,
                    "dateTimeISO": "2022-12-06T10:00:00-06:00",
                    "tempC": -8.3,
                    "tempF": 17.06,
                    "feelslikeC": -10.99,
                    "feelslikeF": 12.23,
                    "dewpointC": -11.42,
                    "dewpointF": 11.44,
                    "humidity": 78,
                    "pressureMB": 1021,
                    "pressureIN": 30.15,
                    "windDir": "SE",
                    "windDirDEG": 140,
                    "windSpeedKTS": 5,
                    "windSpeedKPH": 9.26,
                    "windSpeedMPH": 5.75,
                    "windGustKTS": 9,
                    "windGustKPH": 16.67,
                    "windGustMPH": 10.36,
                    "precipMM": 0,
                    "precipIN": 0,
                    "precipRateMM": 0,
                    "precipRateIN": 0,
                    "snowCM": 0,
                    "snowIN": 0,
                    "snowRateCM": 0,
                    "snowRateIN": 0,
                    "pop": 0,
                    "visibilityKM": 24.135,
                    "visibilityMI": 14.997,
                    "sky": 40,
                    "cloudsCoded": "SC",
                    "weather": "Partly Cloudy",
                    "weatherCoded": "::SC",
                    "weatherPrimary": "Partly Cloudy",
                    "weatherPrimaryCoded": "::SC",
                    "icon": "pcloudy.png",
                    "solradWM2": 248,
                    "uvi": 0,
                    "isDay": true,
                    "spressureMB": 988.3,
                    "spressureIN": 29.18,
                    "altimeterMB": 1018.2,
                    "altimeterIN": 30.07,
                    "solrad": {
                        "azimuthDEG": 150.0833,
                        "zenithDEG": 73.1983,
                        "ghiWM2": 247.6449,
                        "dniWM2": 675.5542,
                        "dhiWM2": 52.3694
                    }
                }
            ],
            "profile": {
                "tz": "America/Chicago",
                "tzname": "CST",
                "tzoffset": -21600,
                "isDST": false,
                "elevM": 253,
                "elevFT": 830
            }
        }
    ]
}"""


def test_data(return_json: bool = False):
    if return_json:
        return raw_data
    return json.loads(raw_data)
