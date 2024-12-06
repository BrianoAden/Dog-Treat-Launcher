# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Music
--------------------------------------------------------------------------
License:   
Copyright 2024 Aden Briano

Based on library from

Copyright 2018 Nicholas Lester

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



"""
import sys

import time
import math
import random

import buzzer

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

TITLE = "title"
NOTES = "notes"


# ------------------------------------------------------------------------
# Note Library
# ------------------------------------------------------------------------
NOTE_B0  = 31
NOTE_C1  = 33
NOTE_CS1 = 35
NOTE_D1  = 37
NOTE_DS1 = 39
NOTE_E1  = 41
NOTE_F1  = 44
NOTE_FS1 = 46
NOTE_G1  = 49
NOTE_GS1 = 52
NOTE_A1  = 55
NOTE_AS1 = 58
NOTE_B1  = 62
NOTE_C2  = 65
NOTE_CS2 = 69
NOTE_D2  = 73
NOTE_DS2 = 78
NOTE_E2  = 82
NOTE_F2  = 87
NOTE_FS2 = 93
NOTE_G2  = 98
NOTE_GS2 = 104
NOTE_A2  = 110
NOTE_AS2 = 117
NOTE_B2  = 123
NOTE_C3  = 131
NOTE_CS3 = 139
NOTE_D3  = 147
NOTE_DS3 = 156
NOTE_E3  = 165
NOTE_F3  = 175
NOTE_FS3 = 185
NOTE_G3  = 196
NOTE_GS3 = 208
NOTE_A3  = 220
NOTE_AS3 = 233
NOTE_B3  = 247
NOTE_C4  = 262
NOTE_CS4 = 277
NOTE_D4  = 294
NOTE_DS4 = 311
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_FS4 = 370
NOTE_G4  = 392
NOTE_GS4 = 415
NOTE_A4  = 440
NOTE_AS4 = 466
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_CS5 = 554
NOTE_D5  = 587
NOTE_DS5 = 622
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_FS5 = 740
NOTE_G5  = 784
NOTE_GS5 = 831
NOTE_A5  = 880
NOTE_AS5 = 932
NOTE_B5  = 988
NOTE_C6  = 1047
NOTE_CS6 = 1109
NOTE_D6  = 1175
NOTE_DS6 = 1245
NOTE_E6  = 1319
NOTE_F6  = 1397
NOTE_FS6 = 1480
NOTE_G6  = 1568
NOTE_GS6 = 1661
NOTE_A6  = 1760
NOTE_AS6 = 1865
NOTE_B6  = 1976
NOTE_C7  = 2093
NOTE_CS7 = 2217
NOTE_D7  = 2349
NOTE_DS7 = 2489
NOTE_E7  = 2637
NOTE_F7  = 2794
NOTE_FS7 = 2960
NOTE_G7  = 3136
NOTE_GS7 = 3322
NOTE_A7  = 3520
NOTE_AS7 = 3729
NOTE_B7  = 3951
NOTE_C8  = 4186
NOTE_CS8 = 4435
NOTE_D8  = 4699
NOTE_DS8 = 4978

# ------------------------------------------------------------------------
# Zelda Song Library
#   - Array of songs 
#     - Each song is a dictionary that has:
#       - TITLE - String title for the song
#       - NOTES - Array of tuples:  (frequency (Hz), length (s), stop (bool))
#
# ------------------------------------------------------------------------
SONGS    = [
    { TITLE  : "Uncover Secret from The Legend of Zelda",
      NOTES  : [(NOTE_G5,  0.150, False), (NOTE_FS5, 0.150, False), (NOTE_DS5, 0.150, False), (NOTE_A4,  0.150, False),
                (NOTE_GS4, 0.150, False), (NOTE_E5,  0.150, False), (NOTE_GS5, 0.150, False), (NOTE_C6,  0.150, True )]
    },
    { TITLE  : "Zelda's Lullaby from The Legend of Zelda",
      NOTES  : [(NOTE_B4,  1.200, False), (NOTE_D5,  0.600, False), (NOTE_A4,  1.800, False), (NOTE_B4,  1.200, False), 
                (NOTE_D5,  0.600, False), (NOTE_A4,  1.800, True )]
    },
    { TITLE  : "Epona's Song from The Legend of Zelda",
      NOTES  : [(NOTE_D5,  0.350, False), (NOTE_B4,  0.350, False), (NOTE_A4,  1.400, False), (NOTE_D5,  0.350, False), 
                (NOTE_B4,  0.350, False), (NOTE_A4,  1.400, False), (NOTE_D5,  0.350, False), (NOTE_B4,  0.350, False),
                (NOTE_A4,  0.700, False), (NOTE_B4,  0.700, False), (NOTE_A4,  1.500, True )]
    },    
    { TITLE  : "Saria's Song from The Legend of Zelda",
      NOTES  : [(NOTE_F4,  0.150, False), (NOTE_A4,  0.150, False), (NOTE_B4,  0.300, False), (NOTE_F4,  0.150, False),
                (NOTE_A4,  0.150, False), (NOTE_B4,  0.300, False), (NOTE_F4,  0.150, False), (NOTE_A4,  0.150, False), 
                (NOTE_B4,  0.150, False), (NOTE_E4,  0.150, False), (NOTE_D5,  0.300, False), (NOTE_B4,  0.150, False),
                (NOTE_C5,  0.150, False), (NOTE_B4,  0.150, False), (NOTE_G4,  0.150, False), (NOTE_E4,  0.600, True )]
    },
    { TITLE  : "Song of Storms from The Legend of Zelda",
      NOTES  : [(NOTE_D4,  0.150, False), (NOTE_F4,  0.150, False), (NOTE_D5,  0.600, False), (NOTE_D4,  0.150, False),
                (NOTE_F4,  0.150, False), (NOTE_D5,  0.600, False), (NOTE_E5,  0.450, False), (NOTE_F5,  0.150, False),
                (NOTE_E5,  0.150, False), (NOTE_F5,  0.150, False), (NOTE_E5,  0.150, False), (NOTE_C5,  0.150, False),
                (NOTE_A4,  0.600, True )]
    },
    { TITLE  : "Sun's Song from The Legend of Zelda.",
      NOTES  : [(NOTE_A4,  0.150, False), (NOTE_F4,  0.150, False), (NOTE_D5,  0.300, True ), (None,     0.300, False),
                (NOTE_A4,  0.150, False), (NOTE_F4,  0.150, False), (NOTE_D5,  0.300, True ), (None,     0.300, False),
                (NOTE_G4,  0.100, False), (NOTE_A4,  0.100, False), (NOTE_B4,  0.100, False), (NOTE_C5,  0.100, False),
                (NOTE_D5,  0.100, False), (NOTE_E5,  0.100, False), (NOTE_F5,  0.100, False), (NOTE_G5,  0.125, False),
                (NOTE_G5,  0.125, False), (NOTE_G5,  0.125, False), (NOTE_G5,  0.125, False), (NOTE_G5,  0.125, False),
                (NOTE_G5,  0.125, False), (NOTE_G5,  0.125, False), (NOTE_G5,  0.125, True )]
    },
    { TITLE  : "Song of Time from The Legend of Zelda",
      NOTES  : [(NOTE_A4,  0.500, False), (NOTE_D4,  1.000, False), (NOTE_F4,  0.500, False), (NOTE_A4,  0.500, False),
                (NOTE_D4,  1.000, False), (NOTE_F4,  0.500, False), (NOTE_A4,  0.250, False), (NOTE_C5,  0.250, False),
                (NOTE_B4,  0.500, False), (NOTE_G4,  0.500, False), (NOTE_F4,  0.250, False), (NOTE_G4,  0.250, False), 
                (NOTE_A4,  0.500, False), (NOTE_D4,  0.500, False), (NOTE_C4,  0.250, False), (NOTE_E4,  0.250, False),
                (NOTE_D4,  1.500, True )]
    },
    { TITLE  : "Minuet of Forest from The Legend of Zelda",
      NOTES  : [(NOTE_D5,  0.225, False), (NOTE_D6,  0.225, False), (NOTE_B5,  0.900, False), (NOTE_A5,  0.225, False),
                (NOTE_B5,  0.225, False), (NOTE_A5,  0.900, True )]
    },
    { TITLE  : "Bolero of Fire from The Legend of Zelda",
      NOTES  : [(NOTE_F4,  0.225, False), (NOTE_D4,  0.225, False), (NOTE_F4,  0.225, False), (NOTE_D4,  0.225, False),
                (NOTE_A4,  0.225, False), (NOTE_F4,  0.225, False), (NOTE_A4,  0.225, False), (NOTE_F4,  0.9375, True )]
    },
    { TITLE  : "Serenade of Water from The Legend of Zelda",
      NOTES  : [(NOTE_D5,  0.500, False), (NOTE_F5,  0.500, False), (NOTE_A5,  0.500, False), (NOTE_A5,  0.500, False),
                (NOTE_B5,  1.000, True )]
    },
    { TITLE  : "Requiem of Spirit from The Legend of Zelda",
      NOTES  : [(NOTE_D5,  0.750, False), (NOTE_F5,  0.375, False), (NOTE_D5,  0.375, False), (NOTE_A5,  0.750, False),
                (NOTE_F5,  0.750, False), (NOTE_D5,  1.500, True )]
    },
    { TITLE  : "Nocturne of Shadow from The Legend of Zelda",
      NOTES  : [(NOTE_B4,  0.670, False), (NOTE_A4,  0.670, False), (NOTE_A4,  0.330, False), (NOTE_D4,  0.330, False),
                (NOTE_B4,  0.330, False), (NOTE_A4,  0.330, False), (NOTE_F4,  1.500, True )]
    },
    { TITLE  : "Prelude of Light from The Legend of Zelda",
      NOTES  : [(NOTE_D5,  0.250, False), (NOTE_A4,  0.750, False), (NOTE_D5,  0.250, False), (NOTE_A4,  0.250, False),
                (NOTE_B4,  0.250, False), (NOTE_D5,  1.250, True )]
    }
]


# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------

class BuzzerMusic():
    buzzer    = None
    song_list = None

    def __init__(self, pin, song_list=None):
    
        self.buzzer = buzzer.Buzzer(pin)
        
        if song_list is not None:
            self.song_list = song_list
        else:
            self.song_list = SONGS
    
    # End def
    
    def play_song_from_list(self, index, title=True, zero_index=False):
        """ Play the song in the song list given the song index.
            By default Python is zero indexed, convert to 1 indexed list 
            zero_index is False.
        """
        # Convert to one indexed value
        if not zero_index:
            index = index - 1

        # Check if index is within the list bounds            
        if (index >= 0) and (index < len(self.song_list)):
            self.play_song(self.song_list[index], title)
        else:
            print("Index out of bounds. Only ")
        
    # End def

    
    def add_song(self, song):
        """ Add a song to the song list """
        self.song_list.append(song)
        
    # End def   
    
    
    def get_song_list_len(self):
        """ Get the length of the song list """
        return len(self.song_list)
    
    # End def
    
    
    def play_song(self, song, title=True, stop=True):
        """ Play a song.
              song  : dictionary with two fields:
                        title : string with title of song
                        list of notes of the format (freq, length, stop)
              title : boolean to indicate if the title should print
              stop  : boolean to indicate if the song should stop at the end 
                (if not already specified in the song)
        """
        try:
            if title:
                print(song[TITLE])
        except:
            print("ERROR:  Song does not have a title field")
        
        try:
            for note in song[NOTES]:
                self.buzzer.play(note[0], note[1], note[2])
        except:
            print("ERROR:  Song does not have notes field")
        
        if stop:
            self.buzzer.stop()
        
    # End def
    
    
    def play_note(self, note, length, stop):
        """ Plays a given note for a given length. 
              If note is None, then the this will rest for the given length
        """
        if note is None:
            time.sleep(length)
        else:
            self.buzzer.play(note, length, stop)
            
    # end def
    
    
    def cleanup(self):
        self.buzzer.cleanup()
    # End def

# End class

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    music = BuzzerMusic("P2_1")
    
    print("Buzzer Music Test")
    
    try:
        for i in range(music.get_song_list_len()):
            print("Play Song {0}".format(i))
            music.play_song_from_list(i, zero_index=True)
    except KeyBoardException:
        pass
        
    music.cleanup()
    
    print("Test Complete")

        