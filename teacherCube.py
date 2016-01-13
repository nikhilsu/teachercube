import RPi.GPIO as GPIO
import time
import os

vibration_sensor_pin = 10
button_pin = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(vibration_sensor_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN)

while 1:
	try:
		if GPIO.input(vibration_sensor_pin) == GPIO.HIGH:
			os.system('espeak "A"')
		if GPIO.input(button_pin) == GPIO.HIGH:
			os.system('espeak "A for aah"')

		time.sleep(1)

	except Exception as e:
		print e.value