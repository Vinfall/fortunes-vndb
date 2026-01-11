#!/usr/bin/env python3
import json
import os
import subprocess
from collections.abc import Generator
from typing import LiteralString
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
    file.writelines(quote + "\n%\n" for quote in fortune_generator(fortunes))

# Generate .dat file
cmd: list[LiteralString] = f"strfile -c % {_OUTPUT_FOLDER + _FORTUNE_FILE}".split()
subprocess.run(cmd, check=True)  # noqa: S603, intended shell injection
