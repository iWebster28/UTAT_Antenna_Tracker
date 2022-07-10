import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)

def forward(sec,loops):
	init()

	direction_bool = True

	for i in range(loops):
		#gpio.output(17, False)
		#gpio.output(22, True)
		gpio.output(23, direction_bool)
		gpio.output(24, not direction_bool)
		print(direction_bool)
		print(not direction_bool)
		print("Changing direction")
		time.sleep(sec)
		direction_bool = not direction_bool

	gpio.cleanup()

def main():
	forward(5,5)
	return 0

if __name__ == "__main__":
	main()
