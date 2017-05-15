'''
Write a program that measures and records temperature temperatures using the
raspberry pi and the attached temperature sensor.

'''

import tempProbe as tp # This is the library for the TempProbe class that we will use
import numpy as np


# This code will create and initialize an instance of an object called probe from the TempProbe class.
probe = tp.TempProbe()

# We will use the get_temp() function from the probe object to return a temperature
probe.get_temp()

# 1.  Write a program that prints the current time and temperature together
#     on one line 
#
# hint: the following command will return the current time:
#
# np.datetime64('now')


# 2. Write a function that writes data to a text file that can be easily
#    read later with pandas, including column headers.
#
# hint: the following code creates a text file that contains two lines.
#
# f = open('testfile.txt','w')
# f.write('a\nb')
# f.close()


# 3. We will run an experiment to measure how well each mug insulates the contents
# Set up your program to record temperature and time to at text file, so we can measure
# the temperature of the water in the mug over the lunch break

# 4. After lunch - Analyze the data
