from numpy import*

x = array(eval(input("valores: ")))

for i in range(shape(x)[0]):
	print(max(x[i, :]))