from numpy import*
from numpy.linalg import*
v = array(eval(input("digite: ")))

quan = array([[50,60,40],[30,40,20],[10,15,8]])
valor = dot(inv(quan), v.T)

print("regular:", round(valor[0],1))
print("ortopedico:",round(valor[1],1))
print("infantil:", round(valor[2],1))
a = min(valor)
if (valor[0]==min(valor)):
	print("regular")
elif (valor[1]== min(valor)):
		print("ortopedico")
elif	(valor[2] == min(valor)):
		print("infantil")

