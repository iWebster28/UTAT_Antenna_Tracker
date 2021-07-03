import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)

def forward(sec):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, True)
	gpio.output(24, True)
	time.sleep(sec)
	gpio.cleanup()

def main():
	forward(5)
	return 0

if __name__ == "__main__":
	main()
