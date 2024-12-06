# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Infrared Sensor
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
This file provides an interface to an infrared sensor.
  - Ex:  https://www.adafruit.com/product/2168


APIs:
  - IR_Sensor(pin)
    - play(frequency, length=1.0, stop=False)
      - Plays the frequency for the length of time

    - stop(length=0.0)
      - Stop the buzzer (will cause breaks between tones)
      
    - cleanup()
      - Stop the buzzer and clean up the PWM

"""

import time

import Adafruit_BBIO.GPIO as GPIO

#constants
HIGH          = GPIO.HIGH
LOW           = GPIO.LOW

class Infrared():
    """Infrared Sensor"""
    pin = None
    
    unbroken_value = None
    broken_value = None
    
    sleep_time = None
    
    unbroken_callback = None
    unbroken_callback_value = None
    broken_callback = None
    broken_callback_value = None
    
    def __init__(self, pin="P1_29", press_low = True, sleep_time = 0.1):
        """Initialize fields and set up IRSensor"""
        if (pin == None):
            raise ValueError("Pin not provided for IRSensor()")
        else:
            self.pin = pin
            # For pull up resistor configuration:    press_low = True
            # For pull down resistor configuration:  press_low = False
        if press_low:
            self.unbroken_value = HIGH
            self.broken_value   = LOW
        else:
            self.unbroken_value = LOW
            self.broken_value   = HIGH
            
            # By default sleep time is "0.1" seconds
        self.sleep_time         = sleep_time
    
            # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Infrared
        GPIO.setup(self.pin, GPIO.IN)

    # End def


    def is_broken(self):
        """ Is the beam broken?
        
           Returns:  True  - beam is broken
                     False - beam is not broken
        """
        # HW#4 TODO: (one line of code)
        #   Remove "pass" and return the comparison of input value of the GPIO pin of 
        #   the buton (i.e. self.pin) to the "pressed value" of the class it
        raw_value = GPIO.input(self.pin)
        print(raw_value)
        return self.broken_value == GPIO.input(self.pin)

    # End def

if __name__ == '__main__':

    print("IR Test")
    
    # Create instantiation of the button
    ir = Infrared("P1_29")

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
        print("Is the beam broken?")
        print("    {0}".format(ir.is_broken()))
    
        print("Break the beam")
        time.sleep(4)
            
        # Check if the button is pressed
        print("Is the beam broken?")
        print("    {0}".format(ir.is_broken()))
            
        print("Close the beam.")
        time.sleep(4)
  
    except KeyboardInterrupt:
        pass
    
    print("Test Complete")

