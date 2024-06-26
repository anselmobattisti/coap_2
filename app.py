#!/usr/bin/env python
# python app.py 192.168.0.150 5683 s1 10 10 10
# python app.py 192.168.0.150 5683 s2 20 20 20
# 1 - CoaP server IP
# 2 - CoaP port
# 3 - Sensor ID, CoaP resource
# 4 - Humidity Limit
# 5 - Temp Limit

import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

path_atuador = "/atuador"

# limite de temperatura
h_lim = int(sys.argv[4])
t_lim = int(sys.argv[5])

path = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/"+sys.argv[3]
host, port, path = parse_uri(path)
led = sys.argv[4]

client = HelperClient(server=(host, port))

# callback do observer
def sensor_observer(response):
    print('Sensor Value Updated')
    global client
    global path_atudador   
    try:
        if response.payload != None:
            print(response.payload)
            print("-----")            
            p = response.payload.split("-")            
            humidity = int(p[0])
            temp = int(p[1])
            if (humidity > h_lim and temp > t_lim):
                response = client.put(path_atuador,led+"-1")
            else:
                response = client.put(path_atuador,led+"-0")
    except NameError:
        print(NameError)
        print('Humidity in not a number')

        
def main():  # pragma: no cover
    global client

    # quando der um PUT no path chama o observer
    client.observe(path, sensor_observer)

if __name__ == '__main__':  # pragma: no cover
    try: 
        main()
    except KeyboardInterrupt:        
        sys.exit()