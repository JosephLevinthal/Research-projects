from numpy import*
pc= input("palavra criptografada: ")
pd=""
i = -1

for ch in pc:
	pd= pd + pc[i]
	i= i - 1
print(pd)
	