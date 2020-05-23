from numpy import *
import numpy as np
p = array(eval(input("")))
q = array(eval(input("")))
a = (p-q)**2
a = np.sum(a)**(1/2)
print(round(a,4))