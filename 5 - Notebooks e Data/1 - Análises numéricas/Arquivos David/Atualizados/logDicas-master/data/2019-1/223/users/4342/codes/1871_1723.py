from numpy import * 
from numpy.linalg import *

mat = array(eval(input('matriz:')))

precototal= round(sum(mat[:,0]*mat[:,1]), 2)
print(precototal)


