from numpy import*
from numpy.linalg import*
n = array(eval(input("Digite os minutos de cada processo: ")))

# x = lavagem minutos
# y = enchimento minutos
# z = rotulo minutos

mat = array([[10,12,9],[4,4,6],[2,1,1]])   #10,4,4 = laranja

c = dot(inv(mat),n.T)

print("laranja: ", round(c[0],0))
print("manga: ", round(c[1],0))
print("abacaxi: ", round(c[2],0))
i =0
if c[0] == min(c):
	print("laranja")
if c[1] == min(c):
	print("manga")
if c[2] == min(c):
	print("abacaxi")