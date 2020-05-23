from numpy import *
from numpy.linalg import *

container=array([[4,5,2],[3,2,2],[2,3,3]])
tipo=array(eval(input()))
tipo=tipo.T
final=dot(inv(container),tipo)

print("grande: ", round(final[0],0))
print("medio: ", round(final[1]))
print("pequeno: ", round(final[2],0))
if final[0]==max(final):
	print('grande')
elif final[1]==max(final):
	print('medio')
else:
	print ('pequeno')
