import RPi.GPIO as GPIO
import time
import os

vibration_sensor_pin = 10
button_pin = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(vibration_sensor_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN)

vibration_sensor_high_counter = 0
button_high_counter = 0

while 1:
	try:
		if GPIO.input(vibration_sensor_pin) == GPIO.HIGH:
			vibration_sensor_high_counter += 1
			if vibration_sensor_high_counter >= 3:
				os.system('espeak "A"')
		else:
			vibration_sensor_high_counter = 0

		if GPIO.input(button_pin) == GPIO.HIGH:
			button_high_counter += 1
			if button_high_counter >= 3:
				os.system('espeak "A for aah"')
		else:
			button_high_counter = 0

		time.sleep(0.3)

	except Exception as e:
		print e.value
