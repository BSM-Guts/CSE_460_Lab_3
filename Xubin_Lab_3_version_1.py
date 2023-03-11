import time
from Motor import *
from Ultrasonic import *
# Here we import the significant functions from the template code
PWM = Motor()
ultrasonic = Ultrasonic()
# Define the distance variable and the gain k and a base speed
# With a base speed the robotic car will not stop when close to target

distance = 50
K = 20
Base_Speed = 800

# The main loop is here.
try:
    while True:
        data = ultrasonic.get_distance()
        print("The distance is "+str(data)+" cm")
        difference = data - distance
        if difference == 0:
            break
        elif difference > 0:
            difference = difference*K
            S = Base_Speed + difference
            PWM.setMotorModel(S, S, S, S)
        else:
            difference = difference*K
            S = Base_Speed + difference
            PWM.setMotorModel(-S, -S, -S, -S)
        time.sleep(0.1)
    # stop the motors
    PWM.setMotorModel(0, 0, 0, 0)


# This block is copied from the template code and modified a for Keyboard Interrupt
except KeyboardInterrupt:
    # when keyboard interrupt we stop the motor
    PWM.setMotorModel(0, 0, 0, 0)
    print("\nProgram end due to Keyboard Interrupt")