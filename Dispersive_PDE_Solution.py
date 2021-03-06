###############################################################################
# Solution to Linear Schrodinger equation
###############################################################################

################################# imports #####################################
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
########################### Initialize variables ##############################
#'''
NFourier = 1000                 # Number of positive fourier coefficients
xstart = pi                     # Starting position to graph the solution at
t = .8745                       # Time to graph solution at
T = "x"                      # String of rational time for data file
T = str(t)                     # String of irrational time for data file
#'''
########################### Define functions ##################################
#'''
def stepFunction1(x):         # 2pi periodic function  
    w = x % (2*pi)
    #print(w)
    if w >= 0 and w < pi:
        return 0
    if w >= pi and w < 2*pi:
        return 1

def w(n):
    return -n**2   
 #''   
#################### Approx. Solution to iut + uxx = 0  #######################
#'''
X = 3000 # Number of points to plot

xlist = np.linspace(xstart,2*pi + xstart,X)
uReal = []
uImag = []

for x in xlist:
    Rsum = 0
    Isum = 0
    n = 0
    #t = x                 # Defining time slice to graph solution at
    while n < NFourier:
        if (n % 2 != 0):
            argpos = n*x + w(n)*t     # Positive argument
            argneg = -n*x + w(-n)*t   # Negative argument
        
            Rsum += (2/n)*np.sin(argpos)
            Rsum += (-2/n)*np.sin(argneg)
            
            Isum += -(2/n)*np.cos(argpos)
            Isum += (2/n)*np.cos(argneg)
        n += 1
    uReal.append(Rsum)
    uImag.append(Isum)
#'''    
############################## Plot ##################################

plt.close()

f, axarr = plt.subplots(2, sharex=True,figsize = (30,10))

axarr[0].plot(xlist, uReal)
axarr[0].set_title("Real part of Linear Schrodinger Solution at t = %s" % T, fontsize=30)
axarr[1].plot(xlist, uImag)
axarr[1].set_title("Imaginary part of Linear Schrodinger Solution at t = %s" % T, fontsize=30)

############################ write lists to files ##############################   
'''
file = open("LinSch_at_t_%s.txt" % T,"w+")

for i in range(len(uReal)):
    R = str(uReal[i])
    I = str(uImag[i])
    X = str(xlist[i])
    file.write("%s,%s,%s \n\r" % (R,I,X))
    
file.close()
'''
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
