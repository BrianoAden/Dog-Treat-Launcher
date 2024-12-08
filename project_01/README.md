<h1>Dog Treat Dispenser</h1>
<p> This project was for my EDES 301 class. Following is a link to the Hackster.io page I put up detailing the physical build of my project.</p>
<a href="https://www.hackster.io/aden-briano/edes301-dog-treat-launcher-bcfb15">Dog Treat Launcher</a>
<p> Now, I will walk you through the software build required to run this project!</p> 


<h2> Setup </h2>
<p> You are going to need to install the operating system on your PocketBeagle. You will need an SD card and SD card flashing software, like Etcher. 
Download bone-debian-10.11-iot-armhf-2022-02-03-4gb.img.xz from <a href="https://rcn-ee.com/rootfs/bb.org/testing/2022-02-03/buster-iot/">OS</a>. 
Use Etcher to flash your SD card. You can now insert your SD card into your PocketBeagle and plug your PocketBeagle into your laptop. 
Great! Now we can get started. You will need to use the Cloud9 IDE to code on the PocketBeagle using Python. Navigate to http://192.168.6.2:3000/ 
in your browser if you're on mac, or http://192.168.7.2:3000/ if you're on windows. You will also need your Beagle to be connected to the internet for this project. 
There are online resources on how to do this, so I won't walk through it. Once you're on Cloud9, run the following commands.</p>
<p>
                                            $ sudo apt-get update <br>
                                            $ sudo apt-get install build-essential python-dev python-setuptools python-smbus -y <br>
                                            $ sudo apt-get install python-pip python3-pip -y <br>
                                            $ sudo apt-get install zip -y <br>
                                            $ sudo pip3 install --upgrade setuptools <br>
                                            $ sudo pip3 install --upgrade Adafruit_BBIO <br>
                                            $ sudo pip3 install adafruit-blinka <br>
</p>
<p>
Now copy this github repo onto your PocketBeagle using the following command <br>
                                            $ git clone https://github.com/BrianoAden/EDES301 <br>
In order to run our project, we need to install the following packages: SpeechRecognition, PyAudio. <br> Let's begin the installation process. Run the following commands. <br>
$ sudo apt-get update <br>
$ sudo apt-get install -y swig libpulse-dev libasound2-dev <br>
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev <br>
$ sudo apt-get python-dev <br>
$ sudo python pyaudio/setup.py install <br>
$ pip3 install SpeechRecognition==3.9.0 <br>

Plug in your USB microphone. Let's check if it's recognized by the PocketBeagle. Run the following command. <br>
$ arecord -l <br>
You should see the following in your output. <br>
card 1: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio] <br>
  Subdevices: 1/1 <br>
  Subdevice #0: subdevice #0 <br>
Good, our microphone is almost ready! We just need to set it as our default device. Run the following command. <br>
$ nano ~/.asoundrc <br>
Now write in the following. <br>

pcm.!default { <br>
        type plug <br>
        slave { <br>
                pcm "hw:0,0" <br>
        } <br>
}<br>
<br>
ctl.!default {<br>
        type hw<br>
        card 0<br>
}<br>

</p>