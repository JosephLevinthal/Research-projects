from numpy import*
from numpy.linalg import*

x = array(eval(input("Matriz:")))
x = x.T
mat1 = zeros(shape(x)[0],dtype = int)
mat2 = zeros(shape(x)[0],dtype = int)
mat3 = zeros(shape(x)[0],dtype = int)
mat4 = zeros(shape(x)[0],dtype = int)

mat1 = sorted(x[0,:], reverse=True)
mat2 = sorted(x[1,:], reverse=True)
mat3 = sorted(x[2,:], reverse=True)
mat4 = sorted(x[3,:], reverse=True)


y = zeros((4,4), dtype=int)

y[:,0] = mat1
y[:,1] = mat2
y[:,2] = mat3
y[:,3] = mat4


print(y)