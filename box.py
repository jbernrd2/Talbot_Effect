import numpy as np
import pandas as pd
from math import log, ceil
def box_dim(x, y, eps):

    df = pd.DataFrame({"X": x, "y": y})

    n_box = 0

    x_interval = (max(x) - min(x))/len(x)

    our_intervals = int((np.pi*2)//eps + 1)

    our_step = eps



    for i in range(our_intervals):

        cur, next_ = eps*i, eps*(i+1)
        df_begin, df_end = cur//x_interval, next_//x_interval
        data = df.iloc[int(df_begin): int(df_end),:]
        if data.shape[0] != 0:
            n_box += ((max(data['y']) - min(data['y']))/eps)
        

    # print(n_box)
    # return log(ceil(n_box))/log(1/eps)

    return log(n_box), log(1/eps)

def test():





    x = np.linspace(0, 2*np.pi, 100000)
    y = np.linspace(0, 7, 100000)

    # print(box_dim(x,y, 0.0001))


    data = pd.read_csv('n1d5t1.csv')


    y,x = [],[]
    for eps in [5e-1, 3e-1, 1e-1, 7e-2, 4e-2, 1e-2, 6e-3, 3e-3, 1e-3, 6e-4]:
        # print(box_dim(data['T'], data['R'], eps))
        _y, _x = box_dim(data['T'], data['R'], eps)
        y.append(_y)
        x.append(_x)

    return y,x
    # df = pd.read_csv('new_data.csv')

    # x = df['T']-3.1415926
    # y = df['R']

    # df = pd.read_csv('RATIONALONEFIFTH.csv')
    
    # x = df['T']- 3.1415926
    # y = df['R']

    #t = x/2
    # data[i*]

test() 

    # y2 = np.cos(x)
    # print(box_dim(x, y2, 1e-4))