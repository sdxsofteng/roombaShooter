# Project: Hacking my Roomba so it can shoot me (with an airsoft gun)

Hello There!

This is a new project where I am trying to hack my IoT vaccum to shoot me with an airsoft gun. I will detail here my tought process and what works and what doesn't. The vaccum is the: Kyvol CyboVac E20 Robot Vaccuum Cleaner.

Enjoy!


# Looking at the Hardware

The vaccuum was pretty simple to take apart. I then realized that approaching this problem on the hardware side was stupid. So I went with the route of capturing Wi-Fi packets sent to the vaccum and reproducing them to make the vaccum do what I wanted it to do.

<img src="images/PXL_20211218_170713944.jpg">


# Capturing Wi-Fi packets

-Setting up system to sniff Wi-Fi packets

https://linuxhint.com/capture_wi-fi_traffic_using_wireshark/

See tutorial to see how I set up Wi-Fi sniffing on my computer.

-Installing and resolving the error in Wireshark

https://linuxhint.com/install-and-use-wireshark-on-manjaro-linux/

It works!! Onto the next thing.

# Analyze Wi-Fi packets sent to and from the Vaccum

The vaccum sends udp updates each 5 seconds, can't seem to decipher them. When I try to see incomig packets. No packets appears after pressing the keys.

# Extracting APK

Extracted the APK using an APK Extractor.

Sent .apk file to Computer.

Converted .apk to .jar with dex2jar

Opened extracted code with JD-GUI

All code is now available to look at in case of need.

Not a lot of valuable information or don't know where to look.

# Using adb to control the app with python.

Downloading and enabling adb for python script in app

I connect using two computers because my main (Manjaro) can't seem to access Pixel Phone
```
Mac:
1) Connect phone
2) Allow
3) adb devices
4) adb tcpip 5555
Main:
5) adb devices
6) adb connect IPADDR:5555
6.1)Accept incoming connection
7) adb devices
```
Sources:
https://stackoverflow.com/questions/31327839/adb-over-wireless-without-usb-cable-at-all-for-not-rooted-phones/31327918

https://help.famoco.com/developers/dev-env/adb-over-wifi/

# Coding in python

Before running script:

Controlling the direction of the robot:

