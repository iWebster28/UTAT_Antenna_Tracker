import RPi.GPIO as GPIO

class Motor():

	IN1 = 24
	IN2 = 23
	#EN = 25

	def __init__(self,IN1=-1,IN2=-1):
		print("Initializing GPIO")
		GPIO.setmode(GPIO.BCM)
		
		# use arbitrary pins if motor input pins not given
		if(IN1>0):
			self.IN1 = IN1
		if(IN2>0):
			self.IN2 = IN2

		# setup GPIO

		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		#GPIO.setup(self.EN,GPIO.OUT)
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		#self.p = GPIO.PWM(self.EN,1000)

	def __del__(self):
		GPIO.cleanup()		

	def rotate(self,direction=1):
		print("Here")
		#self.p.ChangeDutyCycle(75)
		if(direction == 1):
			GPIO.output(self.IN1,GPIO.HIGH)
			GPIO.output(self.IN2,GPIO.LOW)
		elif(direction == -1):
			GPIO.output(self.IN1,GPIO.LOW)
			GPIO.output(self.IN2,GPIO.HIGH)

if(__name__=="__main__"):
	print("hello")
	m = Motor()

	m.rotate(-1)
	while(1):
		pass
	
