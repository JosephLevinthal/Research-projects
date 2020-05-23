from numpy import*
s = input("Digite uma string: ")
new = s.replace(" ", "")
inv = ""
i = -1
while(i >= -len(new)):
	inv = inv + new[i]
	i = i - 1
print(new.upper())
if(inv == new):
	print(1)
else:
	print(0)