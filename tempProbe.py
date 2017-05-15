import os, sys, glob, time
import numpy as np
class TempProbe(object):
    ''' Class controls the 1-wire temperature probe when connected to a raspberry pi

        This class handles the setup and formatting involved in retrieving a
        temperature reading from a temperature sensor based on the 1-wire sensor
        protocol.

        Attributes:
            sn (str): the hardware address for the probe
            tmp_raw (str): unprocesses values from the probe
            tmp (float): The last requested temperature

        The conversion of raw str to a temperature value is based on code from:
        https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview
        written by Simon Monk


    '''

    def __init__(self):
        '''
        The setup function is used to initialize the object, this method si called
        when the object is first initialzed.
        '''
        self.sn = ""
        self.tmp_raw = ""
        self.tmp = 0.0
        self.setup()

    def setup(self):
        '''Housekeeping for using sensor on Raspberry pi.

            The os.system() function is the same as running the string as a
            command in the terminal

            modprobe w1-gpio - added the w1-gpio module to the linux kernal.
            This handles all of the backend.
        '''
        try:
            os.system('modprobe w1-gpio')
            os.system('modprobe w1-therm')
            self.sn = self.find_probe()
            print('Initializing probe ',self.sn)
        except Exception as e:
            print("Are the probes plugged in?")
            sys.exit('Shutting down')

    def find_probe(self):
        ''' Find the mac address for the probe. Assuming it starts with 28-'''
        probes = glob.glob('/sys/bus/w1/devices/28-*')
        if len(probes):
            pick = 0
        elif len(probes) > 1: # if more than one probe is being used
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
        '''
        Formats the raw_temp
        '''

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

if __name__ == '__main__':
    probe = TempProbe()
    print('Temp:',probe.get_temp(),'C')
