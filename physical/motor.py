import RPi.GPIO as GPIO

class Motor():

	IN1 = 24
	IN2 = 23
	EN = 25

	def __init__(self):
		print("Initializing GPIO")
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		GPIO.setup(self.EN,GPIO.OUT)
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		self.p = GPIO.PWM(self.EN,1000)

	def __del__(self):
		GPIO.cleanup()		

	def main(self):
		print("Here")
		self.p.ChangeDutyCycle(75)
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)

if(__name__=="__main__"):
	print("hello")
	m = Motor()

	m.main()
	while(1):
		pass
