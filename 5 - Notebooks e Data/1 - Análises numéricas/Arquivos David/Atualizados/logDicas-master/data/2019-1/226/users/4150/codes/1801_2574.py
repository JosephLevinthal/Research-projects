from numpy import*

s = input("qual a sua senha:")

i = 0 
for i in s:
	if size(s)>=8:
		i = "SENHA VALIDA"
	elif s[i] == s[i].isupper():
		i = "SENHA VALIDA"
	elif s[i] == s[i].islower():
		i = "SENHA VALIDA"
print(i)