import os, sys, glob, time
import numpy as np
class TempProbe():

    def __init__(self):
        self.sn = ""
        self.tmp_raw = ""
        self.tmp = 0.0
        self.setup()

    def setup(self):
        # Housekeeping for using sensor on Raspberry pi
        try:
            os.system('modprobe w1-gpio')
            os.system('modprobe w1-therm')
            self.sn = self.find_probe()
        except Exception as e:
            print("Are the probes plugged in?")
            sys.exit('Shutting down')       

    def find_probe(self):
        ''' Find the mac address for the probe. Assuming it starts with 28-'''
        probes = glob.glob('/sys/bus/w1/devices/28-*')
        if len(probes) > 1: # if more than one probe is being used
            for i, p in enumerate(probes):
                  print(i,':',p)
            pick = int(input('Which probe? (ie 0,1...)'))
        return probes[pick]

    
    def __get_raw_temp__(self):
        '''
        Returns the raw string text for the temperature probe
        '''
        try:
            f = open(self.sn+'/w1_slave','r')
            lines = f.readlines()
            f.close()
            self.tmp_raw = lines      
        except Exception as e:
            print(e)
            self.tmp_raw = 'NULL'      
                  
    def get_temp(self):
        self.__get_raw_temp__()
        lines = self.tmp_raw
        while lines[0].strip()[-3:] != "YES":
            time.sleep(0.2)
            lines = temp_raw()
        temp_output = lines[1].find('t=')
        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output+2:]
            temp_c = float(temp_string) / 1000.0
            self.tmp = temp_c
            return temp_c

