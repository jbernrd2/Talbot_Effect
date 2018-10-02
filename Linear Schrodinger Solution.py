###############################################################################
# Solution to Linear Schrodinger equation
###############################################################################

################################# imports #####################################
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
########################### Define functions ##################################

def stepFunction1(x):         # 2pi periodic function  
    w = x % (2*pi)
    #print(w)
    if w >= 0 and w < pi:
        return 0
    if w >= pi and w < 2*pi:
        return 1
    
def stepFunction2(x):         # 2pi periodic function  
    w = x % (2*pi)
    #print(w)
    if w >= 0 and w < pi:
        return -1
    if w >= pi and w < 2*pi:
        return 1
    
########################### Initialize variables ##############################

NFourier = 500                 # Number of positive fourier coefficients
Gn_real = np.zeros(NFourier+1) # Array of fourier coefficients An
Gn_imag = np.zeros(NFourier+1) # Array of fourier coefficients Bn
K = 500                        # Number of iterations for fourier coefficients
a0 = 1/2                       # Initial Fourier coefficient 
t = 0.3

##################### Calculate Fourier Coefficients ##########################

for n in np.arange(1,NFourier + 1,1):
    Rsum = 0
    Isum = 0
    for x in np.linspace(0,2*pi,K):
        Rsum += stepFunction1(x)*np.cos(n*x)
        Isum += stepFunction1(x)*np.sin(n*x)
    Gn_real[n] = 1/(80)*Rsum
    Gn_imag[n] = 1/(80)*Isum

############################## Approximation of stepFunction1 #########################################
'''
X = 500 # Number of points to plot

xlist = np.linspace(0,2*pi,X)
ylist = []
for j in np.arange(X):
    x = xlist[j] 
    sum = 0
    for n in np.arange(NFourier):
        sum += Gn_real[n]*np.cos(n*x) + Gn_imag[n]*np.sin(n*x)
    ylist.append(sum )

plt.plot(xlist,ylist)

'''
############################## Approx. Solution  ##############################
#'''
X = 500 # Number of points to plot

xlist = np.linspace(0,2*pi,X)
uReal = []
uImag = []
n = 1

for x in xlist:
    Rsum = 0
    Isum = 0
    n = 0
    while n < NFourier:
        arg = n*x - n*n*t
        Rsum += Gn_real[n]*np.cos(arg)
        Isum += Gn_imag[n]*np.sin(arg)
        n += 1
    uReal.append(Rsum)
    uImag.append(Isum)
    
plt.figure(figsize=(30,10))
plt.plot(xlist,uReal)
#'''   
####################### Chen-Olver Solution ###################################
'''
X = 500 # number of points to plot
t = 0.1*pi # time in seconds
p = 1   # power of the pde
xlist = np.linspace(0,2*pi,X)
ylist = []

for x in xlist:
    arg = t*(np.abs(stepFunction2(x)))**p
    Re_y = stepFunction2(x)*np.cos(arg)
    Im_y = stepFunction2(x)*np.sin(arg)
    ylist.append(Re_y)
    
plt.plot(xlist,ylist)
'''    

    

        
        
    