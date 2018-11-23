###############################################################################
# PDEsolutionWithBoxDimension
#       This file defines all the functions needed to provide an analytic 
#       solution to a dispersive PDE, to plot the solutions, and to calculate
#       the box dimension of the solution curves
#       All of the functions have comments above them that describe the inputs
#       to the functions. If you are having trouble, or want to ask any 
#       questions feel free to contact me whenever: 630-696-6506
###############################################################################
# imports
import numpy as np
import matplotlib.pyplot as plt
from math import log, ceil
from scipy import stats
import pandas as pd

pi = np.pi
######################### Define Functions ####################################
###############################################################################

#################################### soln #####################################
# The solution will be graphed as a function of position, at a specific time
# The time is defined as: t = slope*x + const
# slope - The slope of the oblique line that the solution is graphed on
#         Set this value to zero to plot at constant time
# const - The constant time offset, or the y intercept in the t equation
# NFourier - The number of positive fourier coefficients to use
# nPoints - The number of points plotted is 2**(nPoints)
#           If nPoints = 10, then 2**10 points will be plotted
# d       -The power in the dispersion relation
# neg     -If true, the dispersion relation will be negative (Ex: the 
#          schrodinger equation has w(n) = -n**2)

def soln(slope, const, NFourier, nPoints, d, neg):
    # Close previous figures
    plt.close(); plt.close(); plt.close()
    
    # Initialize variables
    X = 2**nPoints
    xlist = np.linspace(0,2*pi,X)
    uReal = []; uImag = []
    m = str(slope); c = str(const); D = str(d)
    
    # Loop through xlist and calculate solution for each x value
    for x in xlist:
        Rsum = 0
        Isum = 0
        n = 0
        t = slope*x + const                # Defining time to graph solution at
        while n < NFourier:
            if (n % 2 != 0):
                argpos = n*x + w(n,d,neg)*t     # Positive argument
                argneg = -n*x + w(-n,d,neg)*t   # Negative argument
                
                Rsum += (2/n)*np.sin(argpos)
                Rsum += (-2/n)*np.sin(argneg)
                
                Isum += (-2/n)*np.cos(argpos)
                Isum += (2/n)*np.cos(argneg)
            n += 1
                
        uReal.append(Rsum)
        uImag.append(Isum)
        
    # Calculate box dimensions, only calculate real box dimension for odd powers
    realBox = box_dim(xlist,uReal,5,"Real Box Dimension")[0]
    print("Box dimension of real part:",realBox)
    if d % 2 != 1:
        imagBox = box_dim(xlist,uImag,5,"Imaginary Box Dimension")[0]
        print("Box dimension of imaginary part:",imagBox)
    
        # Plot Solutions
        f, axarr = plt.subplots(2, sharex=True,figsize = (30,10))
        
        axarr[0].plot(xlist, uReal); axarr[1].plot(xlist, uImag)
        axarr[0].set_title("Real part of w(n) = n^%s Solution at t = %s*x + %s : BD = %s" %(D,m,c,str(realBox)[0:-5]), fontsize=30)         
        axarr[1].set_title("Imaginary part of w(n) = n^%s Solution at t = %s*x + %s : BD = %s" %(D,m,c,str(imagBox)[0:-5]), fontsize=30)
    
    # If odd powered dispersion relation, only plot real part
    else:
        plt.figure(figsize = (30,10)); plt.plot(xlist,uReal);
        plt.title("Real part of w(n) = n^%s Solution at t = %s*x + %s : BD = %s" %(D,m,c,str(realBox)[0:-5]), fontsize=30)       

############################## listReturn #####################################
# Takes data as input and returns one column of the data as a list

# Parameters:
#       data - Enter the data file
#   
#       index - 0 for real, 1 for imaginary, or 2 for x
 
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

################################## w(n,d) #####################################
# Defines the dispersion relation, that takes d as the power of the relation
# Set third argument as true to return negative dispersion relation (like sch.)

def w(n,d,neg):
    if neg == True:
        return -n**d
    else:
        return n**d
    
################################# box_dim #####################################
# Takes input of (x,y) coordinates, and the number of box dimension points to 
# plot, and returns a graph of the box dimension points, and uses slope of the
# best fit line to approximate the box dimension

# Inputs:
#   x - the list of x coordinates 
#   y - the list of y coordinates
#   n - number of box dimension points to plot
#   title - title of the graph

def box_dim(x, y, n, title):
     # Check for invalid inputs
    if type(n) != int:
        print("n must be an integer")
        return
    if len(x) != len(y):
        print("x and y lists must have same size")
        
    # Assign variables
    dx = (max(x) - min(x))/len(x)
    emin = 5*dx + 0.001
    elist = []
    
    
    df = pd.DataFrame({"X": x, "y": y})
    
    # create epsilon list
    for i in range(n):
        elist.append(emin**(1/(i+1)))
        
    # Calculate box dimensions for various epsilons  
    lognbox = []; logeps = []    
    for i in elist:
        eps = i
        our_intervals = int((np.pi*2)/eps + 1)
        n_box = 0
        for j in range(our_intervals):

            cur, next_ = eps*j, eps*(j+1)
            df_begin, df_end = cur//dx, next_//dx
            data = df.iloc[int(df_begin): int(df_end),:]
            if data.shape[0] != 0:
                n_box += ((max(data['y']) - min(data['y']))/eps)
                
            #print(n_box)
        
        if n_box > 1e-7:
            lognbox.append(log(n_box)); logeps.append(log(1/eps)) 

    plt.figure()
    plt.plot(logeps,lognbox,'.r'); plt.title(title) 
    return stats.linregress(logeps,lognbox)

############################ Run the solution #################################
# Running "soln()" will calculate the solution, graph it, and calculate box dimensions
# soln(slope,const,NFourier,nPoints,d,neg)
soln(  0,    0.1*pi,    1000,    15,   3, False)
    