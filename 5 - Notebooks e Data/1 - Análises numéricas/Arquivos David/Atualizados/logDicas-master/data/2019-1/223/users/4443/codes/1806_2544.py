from numpy import *
ve = array(eval(input("Digite o tamanho das batatas: ")))
vs = zeros(3, dtype=int)
for i in ve:
	if(i >= 10):
		vs[0] = vs[0]+1
	elif(5 <= i < 10):
		vs[1] = vs[1]+1
	elif(i < 5):
		vs[2] = vs[2] +1
print(vs[0])
print(vs[1])
print(vs[2])