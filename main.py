import json

# Specify the path to your JSON file
file_path = "config.json"

# Open the JSON file and load its contents
with open(file_path) as file:
	data = json.load(file)
	print(data["gpio-red"])
	print(data["gpio-green"])
	print(data["gpio-blue"])

