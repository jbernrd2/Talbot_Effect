###################### Code for opening Data files ############################
# This code takes a data file from a PDE solution, and returns the real and 
# imaginary parts of the solution, as well as the position that each of these
# data points as an array 
###############################################################################

# data: The data file that you wish to access 
# index: 0 or 'real' for real part of solution
#        1 or 'imag' for imaginary part of solution
#        2 or 'x' for x position

def listReturn(data,index):
    # Check the type of inputs
    if type(index) == str:
        index = index.upper()
        if index == 'REAL':
            index = 0
        elif index == 'IMAG':
            index = 1
        elif index == 'X':
            index = 2
        else:
            print('Invalid argument for input: index')
            return 0
    elif type(index) == int:
        if index < 0 and index > 2:
            print('Invalid argume for input: index')
        
    output = []
    with open(data) as f:
        file = f.readlines()
        for i in file:
            line = i.strip().split(',')
            if len(line) != 1:
                output.append(float(line[index]))
    return output

import numpy as np
import matplotlib.pyplot as plt 
#plt.plot(listReturn('LinSch_at_t_0.3x.txt','Real'))
