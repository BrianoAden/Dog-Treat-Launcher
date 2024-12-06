# """
# --------------------------------------------------------------------------
# Servo Driver
# --------------------------------------------------------------------------
# License:   
# Copyright 2024 Aden Briano

# Based on library from

# Copyright 2024 Erik Welsh

# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this 
# list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors 
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# --------------------------------------------------------------------------

# FS5103R Continuous Rotation Servo Driver

# API:
#   ContinuousRotationServo(pin)
#     - Provide pin that the ContinuousRotationServo is connected
  
#     turn(percentage)
#       -   0 = Fully clockwise
#       - 100 = Fully anti-clockwise

# """
# import Adafruit_BBIO.PWM as PWM

# # ------------------------------------------------------------------------
# # Constants
# # ------------------------------------------------------------------------

# FS51_FREQ               = 50                  # 20ms period (50Hz)
# FS51_POL                = 0                   # Rising Edge polarity
# FS51_MIN_DUTY           = 5                   # 1ms pulse (5% duty cycle)  -- Fully clockwise (right)
# FS51_MID_DUTY           = 7.5                 # 1.5ms pulse (7.5% duty cycle) -- Stops
# FS51_MAX_DUTY           = 10                  # 2ms pulse (10% duty cycle) -- Fully anti-clockwise (left)

# # ------------------------------------------------------------------------
# # Global variables
# # ------------------------------------------------------------------------

# # None

# # ------------------------------------------------------------------------
# # Functions / Classes
# # ------------------------------------------------------------------------

# class ContinuousRotationServo():
#     """ Flywheel Launcher """
    
#     pin = None
#     power = None
    
#     def __init__(self, pin=None, default_power=0):
#         """ Initialize variables and set up the ContinuousRotationServo """
#         if (pin == None):
#             raise ValueError("Pin not provided for ContinuousRotationServo()")
#         else:
#             self.pin = pin

#         self.power = default_power
        
#         self._setup(default_power)
    
#     # End def
    
    
#     def _setup(self, default_power):
#         """Setup the hardware components."""
#         # Initialize ContinuousRotationServo; ContinuousRotationServo should be "off"
        
#         PWM.start(self.pin, FS51_MID_DUTY, FS51_FREQ, FS51_POL)
        
#         # # Set default position
#         self.turn(default_power)

#     # End def

    
#     def _duty_cycle_from_power(self, power):
#          """ Return the duty cycle to set the provided power """
#          return ((FS51_MID_DUTY - FS51_MAX_DUTY) * (power / 100)) + FS51_MID_DUTY    
        
#     # End def
    
    
#     def get_power(self):
#         """ Return the power of the continuous rotation servo """
#         return self.power
    
#     # End def
    
#     def turn(self, power):
#         """ Turn Servo with desired power
        
#             100 = Fully clockwise (right)
#             -100 = Fully counterclockwise (left)      
#         """
#         # Record the current position
#         self.power = power
        
#         # Set PWM duty cycle based on position
#         duty_cycle = self._duty_cycle_from_power(power)
        
#         PWM.set_duty_cycle(self.pin, duty_cycle)
        
#     #End def

#     def cleanup(self):
#         """Cleanup the hardware components."""
#         # Stop servo
#         PWM.stop(self.pin)
#         PWM.cleanup()
        
#     # End def

# # End class



# # ------------------------------------------------------------------------
# # Main script
# # ------------------------------------------------------------------------

# if __name__ == '__main__':
#     import time
    
#     print("Servo Test")

#     # Create instantiation of the servo
#     servo = ContinuousRotationServo("P1_36")

#     # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
#     print("Use Ctrl-C to Exit")
    
#     try:
#         while(1):
#             # Turn Servo anti-clockwise
#             servo.turn(-100)
#             print("Current power = {0}%".format(servo.get_power()))
#             time.sleep(1)
            
#             # Turn Servo clockwise
#             servo.turn(100)
#             print("Current power = {0}%".format(servo.get_power()))
#             time.sleep(1)
            
#             # Stop Servo
#             servo.turn(0)
#             print("Current power = {0}%".format(servo.get_power()))
#             time.sleep(1)
        
#     except KeyboardInterrupt:
#         pass

#     # Clean up hardware when exiting
#     servo.cleanup()

#     print("Test Complete")

"""
--------------------------------------------------------------------------
Servo Driver
--------------------------------------------------------------------------
License:   
Copyright 2024 Aden Briano

Based on Servo library from

Copyright 2024 Erik Welsh

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

SG90 Servo Driver

API:
  Servo(pin)
    - Provide pin that the Servo is connected
  
    turn(percentage)
      -   0 = Fully clockwise
      - 100 = Fully anti-clockwise

"""
import Adafruit_BBIO.PWM as PWM

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

SG90_FREQ               = 50                  # 20ms period (50Hz)
SG90_POL                = 0                   # Rising Edge polarity
SG90_MIN_DUTY           = 5                   # 1ms pulse (5% duty cycle)  -- Fully clockwise (right)
SG90_MAX_DUTY           = 10                  # 2ms pulse (10% duty cycle) -- Fully anti-clockwise (left)

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Servo():
    pin       = None
    position  = None
    
    def __init__(self, pin=None, default_position=35):
        """ Initialize variables and set up the Servo """
        if (pin == None):
            raise ValueError("Pin not provided for Servo()")
        else:
            self.pin = pin

        self.position = default_position
        
        self._setup(default_position)
    
    # End def
    
    
    def _setup(self, default_position):
        """Setup the hardware components."""
        # Initialize Servo; Servo should be "off"
        
        PWM.start(self.pin, SG90_MIN_DUTY, SG90_FREQ, SG90_POL)
        
        # Set default position
        self.turn(default_position)

    # End def

    
    def _duty_cycle_from_position(self, position):
        """ Return the duty cycle to set the provided position """
        return ((SG90_MAX_DUTY - SG90_MIN_DUTY) * (position / 100)) + SG90_MIN_DUTY    
        
    # End def
    
    
    def get_position(self):
        """ Return the position of the servo """
        return self.position
    
    # End def
    

    def turn(self, position):
        """ Turn Servo to the desired position based on percentage of motion range
        
              0% = Fully clockwise (right)
            100% = Fully anti-clockwise (left)      
        """
        # Record the current position
        self.position = position
        
        # Set PWM duty cycle based on position
        duty_cycle = self._duty_cycle_from_position(position)
        
        PWM.set_duty_cycle(self.pin, duty_cycle)

    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
        # Stop servo
        PWM.stop(self.pin)
        PWM.cleanup()
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    import time
    
    print("Servo Test")

    # Create instantiation of the servo
    servo = Servo("P2_3")

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    print("Use Ctrl-C to Exit")
    
    try:
        while(1):
            # Turn Servo anti-clockwise
            servo.turn(35)
            print("Current position = {0}%".format(servo.get_position()))
            time.sleep(0.5)
        
            servo.turn(100)
            print("Current position = {0}%".format(servo.get_position()))
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        pass

    # Clean up hardware when exiting
    servo.turn(0)
    servo.cleanup()

    print("Test Complete")

