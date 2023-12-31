import json

# Specify the path to your JSON file
file_path = "config.json"

# Open the JSON file and load its contents
with open(file_path) as file:
	data = json.load(file)
	gpio_red = data["gpio-red"]
	gpio_green = data["gpio-green"]
	gpio_blue = data["gpio-blue"]

