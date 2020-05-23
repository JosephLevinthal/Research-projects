from numpy import *
s = input("Digite aqui a sua string: ").lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for z in range(len(s)):
	if (s[z] == "a"):
		a = a + 1
	elif (s[z] == "e"):
		e = e + 1
	elif (s[z] == "i"):
		i = i + 1
	elif (s[z] == "o"):
		o = o + 1
	elif (s[z] == "u"):
		u = u + 1
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)
	