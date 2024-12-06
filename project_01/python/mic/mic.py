"""
--------------------------------------------------------------------------
AudioDetector
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
This file provides an interface to a USB Mini Microphone.


APIs:
  - AudioDetector()
    - record
      - uses speech_recognition and pyaudio to recognize and interpret audio
"""
import time

import speech_recognition as sr
import pyaudio
import pocketsphinx

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------

class AudioDetector():
    
    command = None
    
    def __init__(self):
        self.command = False
        
    def reset(self):
        self.command = False
        
    def set_command(self, boolean):
        if not isinstance(boolean, bool):
            raise ValueError("Expected a boolean value for 'command'")
        else:
            self.command = boolean
    
    def detect(self):
        # obtain audio from the microphone
        
        r = sr.Recognizer()
        with sr.Microphone(device_index = 0) as source:
            r.energy_threshold = 300
            r.dynamic_energy_threshold = True
            print("Say something!")
            audio = r.listen(source)
        
        # recognize speech using google speech recognition
        try:
            if r.recognize_google(audio) == "start the game":
                print(r.recognize_google(audio))
                self.set_command(True)
                return self.command
            else:
                print(r.recognize_google(audio))
                self.set_command(False)
                return self.command
        except Exception:
            print(r.recognize_google(audio))
            self.set_command(False)
            self.detect()
            return self.command
        
    
# End class

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    mic = AudioDetector()
    mic.detect()

