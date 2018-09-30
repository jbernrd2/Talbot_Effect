###############################################################################
# Reconstruction of graphs from Olver_AMM
###############################################################################
######################### imports #############################################
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
########################  Functions  ##########################################

# stepFunction1 - 2 pi periodic function
# f(t) = 0 for 0 < x < pi and f(x) = 1 for pi < x < 2*pi
def stepFunction1(x):
    w = x % 2*pi
    if w >= 0 and w < pi:
        return 0
    if w >= pi and w < 2*pi:
        return 1

# stepFunction2 - 2 pi periodic function
# f(t) = -1 for 0 < x < pi and f(x) = 1 for pi < x < 2*pi
def stepFunction2(x):
    w = t % 2*pi
    if w >= 0 and w < pi:
        return -1
    if w >= pi and w < 2*pi:
        return 1
    
##################### Initialize Variables/Lists ##############################

N = 500
t = .05
tstep = 0.1
j = 0
n = np.arange(N)
x = np.linspace(0,2*pi,N)
u = np.zeros(N)

####################### Calculate solution values 1 ###########################

for i in n:
    print(i)
    sum = 0; j = 0
    while j < 1000:
        sum += (np.sin((2*j + 1)*x[n] - ((2*j + 1)**3)*t))/(2*j + 1)
        j += 1 
    u[n] = 1/2 - (2/pi)*sum

plt.gcf().clear()
plt.figure(1)
plt.title("t = 1/33*pi")
plt.plot(x,u)
plt.show()



    
    
    
    
    
    
    
    
    