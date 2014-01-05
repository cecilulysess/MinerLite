# MinerLite - A client side miner controller. 
# This will launch cgminer with a few delay seconds and 
# retrieve the local data and post it into somewhere!
#
# Author: Yanxiang Wu
# Release Under GPL 3 
# Used code from cgminer python API example

import socket
import json
import sys
from subprocess import call
import time

def linesplit(socket):
        buffer = socket.recv(4096)
        done = False
        while not done:
                more = socket.recv(4096)
                if not more:
                        done = True
                else:
                        buffer = buffer+more
        if buffer:
                return buffer


def retrieve_cgminer_info(command, parameter):
        """retrieve status of devices from cgminer
        """

        api_ip = '192.168.0.27'
        api_port = 4028

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((api_ip,int(api_port)))
        if not parameter:
                s.send(json.dumps({"command":command,"parameter":parameter}))
        else:
                s.send(json.dumps({"command":command}))

        response = linesplit(s)
        response = response.replace('\x00','')
        return_val = response
        response = json.loads(response)
        print response
        s.close()
        return return_val

def run_cgminer(path):
        call([path, "--api-listen"])



path = "~/mining/cgminer/cgminer"

print "Starting cgminer in 2 seconds"
time.sleep(2)
print "Running cgminer ..."
run_cgminer(path)
time.sleep(5)
print "Try to retrieve running status:"
retrieve_cgminer_info("devs", None)