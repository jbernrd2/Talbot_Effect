###############################################################################
# PDEsolutionWithBoxDimension
###############################################################################
# imports
from BoxDimenAndGraph import box_dim,listReturn
import numpy as np
import matplotlib.pyplot as plt
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

def soln(slope, const, NFourier, nPoints,d):
    # Close previous figures
    plt.close(); plt.close()
    
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
                argpos = n*x + w(n,d)*t     # Positive argument
                argneg = -n*x + w(-n,d)*t   # Negative argument
                
                Rsum += (2/n)*np.sin(argpos)
                Rsum += (-2/n)*np.sin(argneg)
                
                Isum += (-2/n)*np.cos(argpos)
                Isum += (2/n)*np.cos(argneg)
            n += 1
                
        uReal.append(Rsum)
        uImag.append(Isum)
    
    # Calculate box dimensions
    realBox = box_dim(xlist,uReal,10)[0]
    imagBox = box_dim(xlist,uImag,10)[0]
    print("Box dimension of real part:",realBox)
    print("Box dimension of imaginary part:",imagBox)
    
    # Plot Solutions
    f, axarr = plt.subplots(2, sharex=True,figsize = (30,10))

    axarr[0].plot(xlist, uReal)
    axarr[0].set_title("Real part of w(n) = n^%s Solution at t = %s*x + %s" %(D,m,c), fontsize=30)
    axarr[1].plot(xlist, uImag)
    axarr[1].set_title("Imaginary part of w(n) = n^%s Solution at t = %s*x + %s" %(D,m,c), fontsize=30)


################################## w(n,d) #####################################        
# d - the power of the dispersion relation
def w(n,d):
    return (-n**d)

soln(1,0,1000,15,2)
    