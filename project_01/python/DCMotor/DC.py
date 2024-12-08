"""
--------------------------------------------------------------------------
DC Motor Driver
--------------------------------------------------------------------------
License:   
Copyright 2024 Aden Briano

Based on library from

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

Adafruit hobby DC motor interface

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

MIN_POWER = 0;
MAX_POWER = 50;

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class DCMotor():
    """ Flywheel Launcher """
    
    pin = None
    power = None
    
    def __init__(self, pin=None, default_power=0):
        """ Initialize variables and set up the DCMotor """
        if (pin == None):
            raise ValueError("Pin not provided for DCMotor()")
        else:
            self.pin = pin

        self.power = default_power
        
        self._setup(default_power)
    
    # End def
    
    
    def _setup(self, default_power):
        """Setup the hardware components."""
        # Initialize DCMotor; DCMotor should be "off"
        PWM.start(self.pin, default_power, 1000, 0)
        
    # End def
    
    def off(self):
        """Turns DC Motor off"""
        
        self.power = MIN_POWER
        PWM.set_duty_cycle(self.pin, MIN_POWER)
    
    def get_power(self):
        """ Return the power of the continuous rotation servo """
        return self.power
    
    # End def
    
    def on(self):
        """ Turn Servo with desired power
        
            100 = Fully clockwise (right)
            -100 = Fully counterclockwise (left)      
        """
        # Record the current power
        self.power = MAX_POWER
        PWM.set_duty_cycle(self.pin, MAX_POWER)
        
    #End def

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
    #servo1 = DCMotor("P1_33")
    servo2 = DCMotor("P1_36")

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    print("Use Ctrl-C to Exit")
    
    try:
        while(1):
            # Turn Servo anti-clockwise
            #servo1.on()
            servo2.on()
            print("Current power = {0}%".format(servo2.get_power()))
            time.sleep(1)
            
            # Turn Servo clockwise
            #servo1.off()
            servo2.off()
            print("Current power = {0}%".format(servo2.get_power()))
            time.sleep(1)
            
            # Stop Servo
            #servo1.on()
            servo2.on()
            print("Current power = {0}%".format(servo2.get_power()))
            time.sleep(1)
        
    except KeyboardInterrupt:
        pass

    # Clean up hardware when exiting
    #servo1.cleanup()
    servo2.cleanup()

    print("Test Complete")

