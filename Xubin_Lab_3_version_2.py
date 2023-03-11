import time
from Motor import *
from Ultrasonic import *
# Here we import the significant functions from the template code
PWM = Motor()
ultrasonic = Ultrasonic()

# Define the distance variable and the gain k
distance = 50
K = 300

# The main loop is here.
try:
    while True:
        data = ultrasonic.get_distance()
        print("The distance is "+str(data)+" cm")
        difference = data - distance
        if difference == 0:
            break
        difference = difference*K
        S = difference
        PWM.setMotorModel(S, S, S, S)
        time.sleep(0.1)
        # stop the motors
    PWM.setMotorModel(0, 0, 0, 0)

# This block is copied from the template code and modified a for Keyboard Interrupt
except KeyboardInterrupt:
    PWM.setMotorModel(0, 0, 0, 0)
    print("\nProgram end due to Keyboard Interrupt")