# Project: Hacking my Roomba so it can shoot me (with an airsoft gun)

Hello There!

This is a new project where I am trying to hack my IoT vaccum to shoot me with an airsoft gun. I will detail here my tought process and what works and what doesn't. The vaccum is the: Kyvol CyboVac E20 Robot Vaccuum Cleaner.

Enjoy!


# Looking at the Hardware

The vaccuum was pretty simple to take apart. I tried checking if the motherboard was a simple arduino but it wasn't. So I went with the route of capturing Wi-Fi packets sent to the vaccum and reproducing them to make the vaccum do what I wanted it to do.

# Capturing Wi-Fi packets

-Setting up system to sniff Wi-Fi packets

https://linuxhint.com/capture_wi-fi_traffic_using_wireshark/

See tutorial to see how I set up Wi-Fi sniffing on my computer.

-Installing and resolving the error in Wireshark

https://linuxhint.com/install-and-use-wireshark-on-manjaro-linux/

![](/images/screenshot.pngscreenshot.png)