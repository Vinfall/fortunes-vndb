local https = require("ssl.https")   -- luasec
local cjson = require("cjson.safe")  -- cjson
local lfs = require("lfs")           -- luafilesystem
local os = require("os")

-- Output files
local output_folder = "output/"
local json_file = "quotes.json"
local fortune_file = "vndb"

-- Get query results
local response_body, response_code = https.request("https://query.vndb.org/5c9a6037d875c238.json")
if response_code ~= 200 then
    error("Failed to get URL: " .. tostring(response_code))
end

local fortunes, err = cjson.decode(response_body)
if err then
    error("Failed to decode JSON: " .. tostring(err))
end

if not lfs.attributes(output_folder) then
    lfs.mkdir(output_folder)
end

local json_file_path = output_folder .. json_file
local json_file_handle = io.open(json_file_path, "w")
json_file_handle:write(cjson.encode(fortunes))
json_file_handle:close()

-- Convert to fortune file format
local function fortune_generator(fortunes)
    local result = {}
    for _, fortune in ipairs(fortunes) do
        table.insert(result, fortune.quote .. "\n\t-- " .. fortune.source)
    end
    return result
end

-- Write fortunes to fortune file
local fortune_file_path = output_folder .. fortune_file
local file_handle = io.open(fortune_file_path, "w")
for _, quote in ipairs(fortune_generator(fortunes)) do
    -- `%` is necessary for fortune file
    file_handle:write(quote .. "\n%\n")
end
file_handle:close()

-- Generate .dat file
os.execute(string.format("strfile -c %% %s", fortune_file_path))
