import json
import time
import RPi.GPIO as GPIO
# Specify the path to your JSON file
file_path = "config.json"

# Open the JSON file and load its contents
with open(file_path) as file:
	data = json.load(file)
	gpio_red = data["gpio-red"]
	gpio_green = data["gpio-green"]
	gpio_blue = data["gpio-blue"]

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_red, GPIO.OUT)
GPIO.setup(gpio_green, GPIO.OUT)
GPIO.setup(gpio_blue, GPIO.OUT)

for i in range(30):
	# Turn on the GPIO pins
	GPIO.output(gpio_red, GPIO.HIGH)
	GPIO.output(gpio_green, GPIO.HIGH)
	GPIO.output(gpio_blue, GPIO.HIGH)
	print("LEDs on")

	# Wait for 1 second
	time.sleep(1)

	# Turn off the GPIO pins
	GPIO.output(gpio_red, GPIO.LOW)
	GPIO.output(gpio_green, GPIO.LOW)
	GPIO.output(gpio_blue, GPIO.LOW)
	print("LEDs off")

	# Wait for 1 second
	time.sleep(1)

# Clean up GPIO
GPIO.cleanup()

