from numpy import *
from numpy.linalg import *
mat = array(eval(input("digite a matriz")))
s= sum(mat)
media= s/size(mat)
print(round(media,2))