# weather
All weather API query and data processing related content

1)
Mapping for WMO weather interpretation codes to german and english

I am using the weather API https://open-meteo.com/en/docs/dwd-api to request location based weather information. It is also possible to get the weather interpretation code with the query. I couldn't find an existing mapping, so I wrote a simple mapper for german and english. If the translation could be better please let me know.

It has one function "weather" that takes the weather code and an optional language. The available languages are defined in the file. If none or invalid is provided, english is used. If the provided weather code is not mapped, it returns the translation of unknown.

At the moment english and german are supported. This will most probably not change from my side.
