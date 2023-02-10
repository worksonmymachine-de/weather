# WMO Weather interpretation codes (WW) as used by https://open-meteo.com/en/docs/dwd-api
# translated by mustbeyourfault@worksonmymachine.de

# Code 	        Description
# 0 	          Clear sky
# 1, 2, 3 	      Mainly clear, partly cloudy, and overcast
# 45, 48 	      Fog and depositing rime fog
# 51, 53, 55 	  Drizzle: Light, moderate, and dense intensity
# 56, 57 	      Freezing Drizzle: Light and dense intensity
# 61, 63, 65 	  Rain: Slight, moderate and heavy intensity
# 66, 67 	      Freezing Rain: Light and heavy intensity
# 71, 73, 75 	  Snow fall: Slight, moderate, and heavy intensity
# 77 	          Snow grains
# 80, 81, 82 	  Rain showers: Slight, moderate, and violent
# 85, 86 	      Snow showers slight and heavy
# 95 * 	          Thunderstorm: Slight or moderate
# 96, 99 * 	      Thunderstorm with slight and heavy hail

ENGLISH = 0
GERMAN = 1

_languages = {
    ENGLISH: 'en',
    GERMAN: 'de'
}
_UNKNOWN = 99999


wmo = {
    'en': {
        0: 'Clear sky',
        1: 'mainly clear', 2: 'partly cloudy', 3: 'overcast',
        45: 'Fog', 48: 'depositing rime fog',
        51: 'light drizzle', 53: 'moderate drizzle', 55: 'dense drizzle',
        56: 'light freezing drizzle', 57: 'dense freezing drizzle',
        61: 'slight rain', 63: 'moderate rain', 65: 'heavy rain',
        66: 'light freezing rain', 67: 'dense freezing rain',
        71: 'slight snow fall', 73: 'moderate snow fall', 75: "heavy snow fall",
        77: 'snow grains',
        80: 'slight rain showers', 81: 'moderate rain showers', 82: 'violent rain showers',
        85: 'slight snow shower', 86: 'heavy snow showers',
        95: 'thunderstorm',
        96: 'thunderstorm with slight hail', 99: 'thunderstorm with heavy hail',
        _UNKNOWN: 'unknown'
    },
    'de': {
        0: 'Klarer Himmel',
        1: 'Größtenteils klar', 2: 'Teilweise wolkig', 3: 'Bedeckt',
        45: 'Nebel', 48: 'Reifnebel',
        51: 'Leichter Nieselregen', 53: 'Mäßiger Nieselregen', 55: 'Starker Nieselregen',
        56: 'Leichter eisiger Nieselregen', 57: 'Starker eisiger Nieselregen',
        61: 'Leichter Regen', 63: 'Mäßiger Regen', 65: 'Starker Regen',
        66: 'Leichter gefrierender Regen', 67: 'Gefrierender Regen',
        71: 'Leichter Schneefall', 73: 'Mäßiger Schneefall', 75: "Starker Schneefall",
        77: 'Schneegraupel',
        80: 'Leichte Regenschauer', 81: 'Mäßige Regenschauer', 82: 'Starke Regenschauer',
        85: 'Leichte Schneeschauer', 86: 'Starke Schneeschauer',
        95: 'Gewitter',
        96: 'Gewitter mit leichtem Hagel', 99: 'Gewitter mit starkem Hagel',
        _UNKNOWN: 'Unbekannt'
    }
}


def weather(code: int, lang=None) -> str:
    lang = _languages[ENGLISH] if lang is None or lang not in _languages.keys() else _languages[lang]
    return wmo[lang][code] if code in wmo[lang].keys() else wmo[lang][_UNKNOWN]


