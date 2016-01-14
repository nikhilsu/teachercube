import RPi.GPIO as GPIO
import time
import os

vibration_sensor_pin = 10
button_pin = 12
connection_pin = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(vibration_sensor_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(connection_pin, GPIO.IN)

vibration_sensor_high_counter = 0
button_high_counter = 0
connection_high_counter = 0

def speak_if_pin_high(pin_to_check, pin_high_counter, string_to_speak):
	
	if GPIO.input(pin_to_check) == GPIO.HIGH:
		pin_high_counter += 1
		if pin_high_counter >= 3:
			os.system("espeak " + string_to_speak)
			pin_high_counter = 0
	else:
		pin_high_counter = 0

	return pin_high_counter	



while 1:
	try:
		vibration_sensor_high_counter = speak_if_pin_high (vibration_sensor_pin, vibration_sensor_high_counter, "A")
		button_high_counter = speak_if_pin_high (button_pin, button_high_counter, "Aah")
		connection_high_counter = speak_if_pin_high (connection_pin, connection_high_counter, "Ad")

		time.sleep(0.3)

	except Exception as e:
		print e.value
