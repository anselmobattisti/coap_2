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
host, port, path_atuador = parse_uri(path)

pixels = [None]*64

client = HelperClient(server=(host, port))

# callback do observer
def atuador_observer():  # pragma: no cover
    # print 'Atuador Value Updated'
    global client
    response = client.get(path_atuador)
    for i in range(64):
        pixels[i] = white
        if response.payload[i] == "1":
            pixels[i] = red
    sense.set_pixels(pixels)        

def main():  # pragma: no cover
    global client  

    while True:    
        time.sleep(1)
        atuador_observer()
        
    # quando der um PUT no path do atuador chama o observer
    # client.observe(path_atuador, atuador_observer)

if __name__ == '__main__':  # pragma: no cover
    main()