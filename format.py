#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import os

# Output files
_OUTPUT_FOLDER = "output/"
_JSON_FILE = "quotes.json"
_FORTUNE_FILE = "vndb"

# Get query results
response = urllib.request.urlopen("https://query.vndb.org/5c9a6037d875c238.json")
fortunes = json.loads(response.read())

os.makedirs(_OUTPUT_FOLDER, exist_ok=True)
with open(_OUTPUT_FOLDER + _JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(fortunes, f)

# Convert to fortune file format
fortune_quotes = []
for fortune in fortunes:
    fortune_quote = f'{fortune["quote"]}\n\t-- {fortune["source"]}'
    fortune_quotes.append(fortune_quote)

with open(_OUTPUT_FOLDER + _FORTUNE_FILE, "w") as file:
    # `%` is necessary for fortune file
    file.write("\n%\n".join(fortune_quotes))

# Generate .dat file
os.system(f"strfile -c % {_OUTPUT_FOLDER + _FORTUNE_FILE}")
