from numpy import*

x=int(input(""))
w="*"
p="o"

for i in range(x):
	f= w*(x-i*1)+p*(2*i)+w*(x-i*1)
	print(f)