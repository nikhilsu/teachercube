import RPi.GPIO as GPIO
import time
import os
import sys

vibration_sensor_pin = 16
button_pin = 20
connection_pin = 21

low_pin = 19
high_pin = 26

alphabet = 'A'
syllable = 'Aah'

GPIO.setmode(GPIO.BCM)

GPIO.setup(vibration_sensor_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(connection_pin, GPIO.IN)

GPIO.setup(low_pin, GPIO.OUT)
GPIO.setup(high_pin, GPIO.OUT)

button_high_counter = 0
connection_high_counter = 0

def speak_if_pin_high(pin_to_check, pin_high_counter, string_to_speak):
	
	if GPIO.input(pin_to_check) == GPIO.HIGH:
		pin_high_counter += 1
		if pin_high_counter >= 3:
			os.system("espeak " + string_to_speak + " 2>/dev/null && echo speaking")
			pin_high_counter = 0
	else:
		pin_high_counter = 0

	return pin_high_counter	


GPIO.output(low_pin, GPIO.LOW)
GPIO.output(high_pin, GPIO.HIGH)

if len(sys.argv) > 1:
	alphabet = str(sys.argv[1])
	syllable = str(sys.argv[2])

while 1:
	try:
		if GPIO.input(vibration_sensor_pin) == GPIO.HIGH:
			os.system("espeak -s 110 '"+ alphabet +"' 2>/dev/null && echo speaking")
		
		button_high_counter = speak_if_pin_high (button_pin, button_high_counter, "-s 110 '"+ alphabet +", for "+ syllable +"'")
		connection_high_counter = speak_if_pin_high (connection_pin, connection_high_counter, "-s 80 'A, T, at'")

		time.sleep(0.5)

	except Exception as e:
		print e.value
