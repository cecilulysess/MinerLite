#!/usr/bin/python

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
import subprocess
import time
import os


path = "/home/ltcminer/mining/cgminer/cgminer"
log_file = "/home/ltcminer/mining/minerlite.log"

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

        api_ip = '127.0.0.1'
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
        # print response
        s.close()
        return return_val

def run_cgminer(path):
        subprocess.Popen([path, "--api-listen"])




print "Starting cgminer in 2 seconds"
time.sleep(2)
print "Running cgminer ..."
run_cgminer(path)
time.sleep(15)
with open(log_file, 'a') as logfile:
        try: 
                logfile.write( retrieve_cgminer_info("devs", None) )
        except socket.error:
                pass