# code source: worksonmymachine.de

# maps a direction angle int to the closest compass direction 'N', 'south-west' and so on
# language en and de is available - default is ENGLISH
# short and long format are available: 'NE', 'north-east' - default is SHORT


ENGLISH = 0
GERMAN = 1
_languages = (ENGLISH, GERMAN)

SHORT = 0
LONG = 1
_types = (SHORT, LONG)

NORTH = 0
NORTH_EAST = 1
EAST = 2
SOUTH_EAST = 3
SOUTH = 4
SOUTH_WEST = 5
WEST = 6
NORTH_WEST = 7

_direction_abbreviations = {
    ENGLISH: {
        NORTH: {SHORT: 'N', LONG: 'north'},
        NORTH_EAST: {SHORT: 'NE', LONG: 'north-east'},
        EAST: {SHORT: 'E', LONG: 'east'},
        SOUTH_EAST: {SHORT: 'SE', LONG: 'south-east'},
        SOUTH: {SHORT: 'S', LONG: 'south'},
        SOUTH_WEST: {SHORT: 'SW', LONG: 'south-west'},
        WEST: {SHORT: 'W', LONG: 'west'},
        NORTH_WEST: {SHORT: 'NW', LONG: 'north-west'}
    },
    GERMAN: {
        NORTH: {SHORT: 'N', LONG: 'nord'},
        NORTH_EAST: {SHORT: 'NO', LONG: 'nordost'},
        EAST: {SHORT: 'O', LONG: 'ost'},
        SOUTH_EAST: {SHORT: 'SO', LONG: 'südost'},
        SOUTH: {SHORT: 'S', LONG: 'süd'},
        SOUTH_WEST: {SHORT: 'SW', LONG: 'südwest'},
        WEST: {SHORT: 'W', LONG: 'west'},
        NORTH_WEST: {SHORT: 'NW', LONG: 'nordwest'}
    }
}


def angle_direction_abbreviation(angle: int, lang: int = None, length: int = None) -> str:
    lang = ENGLISH if lang is None or lang not in _languages else lang
    length = SHORT if length is None or length not in _types else length
    return _direction_abbreviations[lang][_map_angle_to_direction(angle)][length]


def _map_angle_to_direction(angle: int) -> int:
    angle = angle % 360
    if angle >= 337 or angle < 23:
        return NORTH
    elif 23 <= angle < 68:
        return NORTH_EAST
    elif 68 <= angle < 113:
        return EAST
    elif 113 <= angle < 158:
        return SOUTH_EAST
    elif 158 <= angle < 203:
        return SOUTH
    elif 203 <= angle < 248:
        return SOUTH_WEST
    elif 248 <= angle < 293:
        return WEST
    elif 293 <= angle < 338:
        return WEST
