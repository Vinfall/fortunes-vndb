#!/usr/bin/env python3

import json
import os
from collections.abc import Generator
from urllib.request import urlopen

# Output files
_OUTPUT_FOLDER = "output/"
_JSON_FILE = "quotes.json"
_FORTUNE_FILE = "vndb"

# Get query results
response = urlopen("https://query.vndb.org/5c9a6037d875c238.json")
fortunes = json.loads(response.read())

os.makedirs(_OUTPUT_FOLDER, exist_ok=True)
with open(_OUTPUT_FOLDER + _JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(fortunes, f)


# Convert to fortune file format
def fortune_generator(fortunes: list[dict]) -> Generator[str, None, None]:
    for fortune in fortunes:
        yield f"{fortune['quote']}\n\t-- {fortune['source']}"


with open(_OUTPUT_FOLDER + _FORTUNE_FILE, "w") as file:
    # `%` is necessary for fortune file
    for quote in fortune_generator(fortunes):
        file.write(quote + "\n%\n")

# Generate .dat file
os.system(f"strfile -c % {_OUTPUT_FOLDER + _FORTUNE_FILE}")  # noqa: S605, intended shell injection
