#!/usr/bin/env python
# python atuador.py 192.168.0.150 5683
# 1 - CoaP server IP
# 2 - CoaP port

import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
white = (255, 255, 255)

path = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/atuador"
host, port, path = parse_uri(path)

pixels = [None]*64

client = HelperClient(server=(host, port))

print path

while True:    
    time.sleep(1)
    response = client.get(path)  
    for i in range(64):
        pixels[i] = white
        if response.payload[i] == "1":
            pixels[i] = red
            
    sense.set_pixels(pixels)        

client.stop()
