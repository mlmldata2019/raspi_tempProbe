'''
Write a program that measures and records temperature temperatures using the
raspberry pi and the attached temperature sensor.

'''

import tempProbe as tp # This is the library for the TempProbe class that we will use
import numpy as np
import datetime as dt


# This code will create and initialize an instance of an object called probe from the TempProbe class.
probe = tp.TempProbe()

# We will use the get_temp() function from the probe obejct to return a temperature
probe.get_temp()

# 1.  write a program that prints the current time and temperature.
# The output should look like this:
# 2017-05-12 21:20:02, 22.34
# hint: there is a datetime function that will return the current time.


# 2. Write a function that writes the date to a text file.


# 3. We will run an experiment to measure how well each mug insulates the contents
# Set up your program to record temperature and time to at text file, so we can measure
# the temperature of the water in the mug over the lunch break

# 4. After lunch - Analyze the data
