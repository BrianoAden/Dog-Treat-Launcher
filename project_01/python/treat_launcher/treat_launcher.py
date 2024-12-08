"""
--------------------------------------------------------------------------
Treat Launcher
--------------------------------------------------------------------------
License:   
Copyright 2024 Aden Briano

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

Use the following hardware components to make a programmable combination lock:  
  - Microphone
  - Button
  - Blue LED
  - Continuoous Rotation Servo
  - DC Motor
  - IR Sensor
  - Buzzer

Requirements:
  - Hardware:
    - When off:   Blue LEDs are off; Buzzer is off; Continous Rotation Servo is "closed"; DC Motor is off; Microphone is on; IR is on
    - When bark detected: One of two Blue LEDS comes on for 10 seconds; Corresponding Button waits for input; Servo is "closed"; DC off; Mic on; IR on
    - When button pressed: LEDs turn off; DC motor on for 1 second; Mic on; IR on; Servo "open"
    - Button
      - Waiting for a button press should allow the display to update (if necessary) and return any values
      - Time the button was pressed should be recorded and returned
    - User interaction:
      - User needs to be able to bark at device
        - Need to be able to press button corresponding to lit LED
      - Treat launcher should release new treat when button is pressed and first treat is launched
      - If bark detected and no button press, return to waiting for bark
      - If there are no treats (IR Sensor returns 0 for 5 seconds), turn on buzzer for 3 seconds, then off for 3, and continue cycle

Uses:
  - Button library developed in class
  - Buzzer library developed in class
  - Servo library developed in class
  - LED library developed in class

"""
from speech_recognition import UnknownValueError
import time
import random as rand
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



from buzzer.buzzer     import Buzzer
from button            import Button
from infrared          import Infrared
from crs               import Servo
from led               import LED
from DC.DC             import DCMotor
from mic.mic           import AudioDetector

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class TreatLauncher():
    """ TreatLauncher """
    reset_time     = None
    blue_button    = None
    yellow_button  = None
    mic            = None
    ir             = None
    blue_led       = None
    yellow_led     = None
    servo          = None
    dc             = None
    buzzer         = None
    debug          = None
    
    def __init__(self, reset_time=2.0, blue_button="P2_2", yellow_button = "P2_4",
                       blue_led="P2_6", yellow_led="P2_8",
                       ir="P1_29", servo="P2_3", dc = "P1_36",
                       buzzer = "P2_1", debug=False):
        """ Initialize variables"""

        self.reset_time     = reset_time
        self.blue_button    = Button(blue_button)
        self.yellow_button  = Button(yellow_button)
        self.blue_led       = LED(blue_led)
        self.yellow_led     = LED(yellow_led)
        self.dc             = DCMotor(dc)
        self.servo          = Servo(servo)
        self.ir             = Infrared(ir)
        self.mic            = AudioDetector()
        self.buzzer         = Buzzer(buzzer)
        self.debug          = debug
    #End def

    def listen(self):
        """
            Listen for command:
               - Turn on either blue_led or yellow_led
               - Start game
        """
        if self.debug:
            print("listen")
        # Randomly choose between LEDS when command detected
        num = rand.randint(1,2)
        try:
            self.buzzer.play(262, 0.25)
            self.buzzer.play(330, 0.25)
            self.buzzer.play(392, 0.25)
            self.buzzer.stop(0.1)
            while self.mic.command == False:
                self.mic.detect()
            if self.mic.command == True:
                if num == 1:
                    self.blue_led.on()
                elif num == 2:
                    self.yellow_led.on()
            return num
        
        except UnknownValueError:
            self.mic.set_command(False)
            self.run()
    # End def
    
    def start_game(self, num):
        """
            Starts game. Depending on LED lit, awaits input from corresponding button.
                - If button pressed. Call launch method.
                - If button is not pressed in 10 seconds, end the game. 
        """
        start_time = time.time()
        elapsed_time = 0
        if num == 1:
            while not self.blue_button.is_pressed() and elapsed_time < 10:
                elapsed_time = time.time() - start_time
            if self.blue_button.is_pressed():
                self.buzzer.play(440, 0.5)
                self.buzzer.stop(0.1)
                self.blue_led.off()
                time.sleep(2)
                self.launch()
            else:
                self.end_game()
        elif num == 2:
            while not self.yellow_button.is_pressed() and elapsed_time < 10:
                elapsed_time = time.time() - start_time
            if self.yellow_button.is_pressed():
                self.buzzer.play(440, 0.5)
                self.buzzer.stop(0.1)
                self.yellow_led.off()
                time.sleep(2)
                self.launch()
            else:
                self.end_game()
    #End def
    
    def end_game(self):
        """
            Ends the game. Turns off all LEDS and calls listen.
                -Will begin listening for command to restart game.
        """
        #preps mic for rerun
        self.yellow_led.off()
        self.blue_led.off()
        self.mic.set_command(False)
        self.run()
    #End def
    
    def launch(self):
        """
            Method to launch treat.
                -Use DC Motor
        """
        if self.debug:
            print("launch")
        self.refill()
        self.dc.on()
        time.sleep(2)
        self.dc.off()
        time.sleep(1)
        self.is_empty()
    #End def
    
    def is_empty(self):
        """
        Method to poll infrared sensors to check if treat supply is empty.
            -If empty, start buzzer for 2 seconds every 10 seconds.
        """
        if self.debug:
            print("is_empty")
        start_time = time.time();
        while self.ir.is_broken() == False:
            print(self.ir.is_broken())
            if time.time() - start_time > 5: 
                self.buzzer.play(3000, length = 3)
                self.buzzer.stop(0.5)
        self.run()
    #End def

    def refill(self):
        """
        Method to refill treat launcher.
        """
        if self.debug:
            print("refill")
        self.servo.turn(100)
        time.sleep(0.5)
        self.servo.turn(35)
        self.mic.set_command(False)
    #End def
    
    def run(self):
        """Main loop for TreatLauncher."""
        try:
            num = self.listen()
            self.start_game(num)
            print("done!")
            
        except KeyboardInterrupt:
            print("Force Stop!")
            self.cleanup()

    # End def

    def cleanup(self):
        """Cleanup the hardware components."""
        

        # Clean up hardware
        self.blue_button.cleanup()
        self.yellow_button.cleanup()
        self.blue_led.cleanup()
        self.yellow_led.cleanup()
        self.servo.cleanup()
        self.buzzer.cleanup()
        self.DC.cleanup()

    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    treat_launcher = TreatLauncher(debug=True)

    try:
        # Run the lock
        treat_launcher.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        treat_launcher.cleanup()

    print("Program Complete")

