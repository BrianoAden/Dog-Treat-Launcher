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
There are online resources on how to do this, so I won't walk through it. Once you're on Cloud9, run the following commands.
                                            sudo apt-get update
                                            sudo apt-get install build-essential python-dev python-setuptools python-smbus -y
                                            sudo apt-get install python-pip python3-pip -y
                                            sudo apt-get install zip -y
                                            sudo pip3 install --upgrade setuptools
                                            sudo pip3 install --upgrade Adafruit_BBIO
                                            sudo pip3 install adafruit-blinka
Now copy this github repo onto your PocketBeagle using the following command
                                            git clone https://github.com/BrianoAden/EDES301
</p>