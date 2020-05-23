from numpy import*
mt=array(eval(input("insira a relacao: ")))
print(mt)
for i in range(shape(mt)[0]):
	print(max(mt[i]))