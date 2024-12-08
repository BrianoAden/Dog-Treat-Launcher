"""
--------------------------------------------------------------------------
Button Driver
--------------------------------------------------------------------------
License:   
Copyright 2024 Aden Briano

Based on library from

Copyright 2020 Erik Welsh

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

Button Driver

  This driver can support buttons that have either a pull up resistor between the
button and the processor pin (i.e. the input is "High" / "1" when the button is
not pressed) and will be connected to ground when the button is pressed (i.e. 
the input is "Low" / "0" when the button is pressed), or a pull down resistor 
between the button and the processor pin (i.e. the input is "Low" / "0" when the 
button is not pressed) and will be connected to power when the button is pressed
(i.e. the input is "High" / "1" when the button is pressed).

  To select the pull up configuration, press_low=True.  To select the pull down
configuration, press_low=False.


Software API:

  Button(pin, press_low)
    - Provide pin that the button monitors
    
    is_pressed()
      - Return a boolean value (i.e. True/False) on if button is pressed
      - Function consumes no time
    
    get_last_press_duration()
      - Return the duration the button was last pressed

    cleanup()
      - Clean up HW
      


"""
import time

import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

HIGH          = GPIO.HIGH
LOW           = GPIO.LOW

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Button():
    """ Button Class """
    pin                           = "P2_2"
    
    unpressed_value               = None
    pressed_value                 = None
    
    sleep_time                    = None
    press_duration                = None
    
    
    def __init__(self, pin="P2_2", press_low=True, sleep_time=0.1):
        """ Initialize variables and set up the button """
        if (pin == None):
            raise ValueError("Pin not provided for Button()")
        else:
            self.pin = pin
        
        # For pull up resistor configuration:    press_low = True
        # For pull down resistor configuration:  press_low = False
        if press_low:
            self.unpressed_value = HIGH
            self.pressed_value   = LOW
        else:
            self.unpressed_value = LOW
            self.pressed_value   = HIGH
        
        # By default sleep time is "0.1" seconds
        self.sleep_time      = sleep_time
        self.press_duration  = 0.0        

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Button
        # HW#4 TODO: (one line of code)
        #   Remove "pass" and use the Adafruit_BBIO.GPIO library to set up the button
        GPIO.setup(self.pin, GPIO.IN)

    # End def


    def is_pressed(self):
        """ Is the Button pressed?
        
           Returns:  True  - Button is pressed
                     False - Button is not pressed
        """
        return self.pressed_value == GPIO.input(self.pin)

    # End def

    
    def get_last_press_duration(self):
        """ Return the last press duration """
        return self.press_duration
    
    # End def
    
    
    def cleanup(self):
        """ Clean up the button hardware. """
        # Nothing to do for GPIO
        pass
    
    # End def
    
# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Button Test")

    # Create instantiation of the button
    button = Button("P2_2")
    
    # Create functions to test the callback functions
    def pressed():
        print("  Button pressed")
    # End def
    
    def unpressed():
        print("  Button not pressed")
    # End def

    def on_press():
        print("  On Button press")
        return 3
    # End def

    def on_release():
        print("  On Button release")
        return 4
    # End def    

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    try:
        # Check if the button is pressed
        print("Is the button pressed?")
        print("    {0}".format(button.is_pressed()))

        print("Press and hold the button.")
        time.sleep(4)
        
        # Check if the button is pressed
        print("Is the button pressed?")
        print("    {0}".format(button.is_pressed()))
        
        print("Release the button.")
        time.sleep(4)
        
        print("Waiting for button press ...")
        button.wait_for_press()
        print("    Button pressed for {0} seconds. ".format(button.get_last_press_duration()))
        
    except KeyboardInterrupt:
        pass

    print("Test Complete")

