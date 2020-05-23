s = input("Digite uma string: ")
# String vazia
new = s.replace(" ","")
inv = ""
# Contador comeca no fim da string
i = -1
while i >= -len(new):
	inv = inv + new[i]
	i = i - 1
	if(new[0:] == inv[0:]):
		a = 1
	else:
		a = 0

print(s.replace(" ","").upper())
print(a)