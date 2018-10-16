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
#'''
NFourier = 1000                 # Number of positive fourier coefficients
Gn_real = np.zeros(NFourier+1) # Array of fourier coefficients An
Gn_imag = np.zeros(NFourier+1) # Array of fourier coefficients Bn
a0 = 1/2                       # Initial Fourier coefficient 
t = pi/7                 # Time to graph solution at
T = "pi/7"            # String of rational time for data file
#T = str(t)                     # String of irrational time for data file
#'''
#################### Approx. Solution to iut + uxx = 0  #######################
#'''
X = 3000 # Number of points to plot

xlist = np.linspace(0,2*pi,X)
uReal = []
uImag = []
n = 1

for x in xlist:
    Rsum = 0
    Isum = 0
    n = 0
    while n < NFourier:
        if (n % 2 != 0):
            argpos = n*x - n*n*t    # Positive argument
            argneg = -n*x - n*n*t   # Negative argument
        
            Rsum += (2/n)*np.sin(argpos)
            Rsum += (-2/n)*np.sin(argneg)
            
            Isum += -(2/n)*np.cos(argpos)
            Isum += (2/n)*np.cos(argneg)
        n += 1
    uReal.append(Rsum)
    uImag.append(Isum)
#'''    
############################ write lists to files ##############################   
'''
file = open("LinSch_step1_%s seconds_750points.txt" % T,"w+")

for i in range(len(uReal)):
    R = str(uReal[i])
    I = str(uImag[i])
    X = str(xlist[i])
    file.write("%s,%s,%s \n\r" % (R,I,X))
    
file.close()
'''
############################## Plot ##################################
#'''
plt.close()
plt.close()
plt.figure(figsize=(30,10))
plt.plot(xlist,uReal)
plt.title("Real part of Linear Schrodinger Solution at t = %s seconds" % T, fontsize=30)

plt.figure(figsize=(30,10))
plt.plot(xlist,uImag)
plt.title("Imaginary part of Linear Schrodinger Solution at t = %s seconds" % T, fontsize = 30)
plt.show()
#'''
######################## Read data files and plot #############################  
'''
xlist = []
uReal = []
uImag = []

with open("LinSch_step1_0.1s_750points.txt") as f:
    file = f.readlines()
    file = [x.strip() for x in file]
    print(file)
        #xlist.append(i[0]); uReal.append(i[1]); uImag.append(i[2])
'''
