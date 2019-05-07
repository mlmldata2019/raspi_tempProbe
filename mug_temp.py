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


# 3. Test the temperature sensor - place the temperature sensor in a cup
#    of warm water and let it adjust to its surroundings. Then place the
#    sensor in a cup of cold water. Record the data for a minute or two.

# 4. Analyze the data to estimate how long it takes to adjust. This can be
#    done in a Jupyter Notebook on your own computer. Compare your estimate
#    with another group.
