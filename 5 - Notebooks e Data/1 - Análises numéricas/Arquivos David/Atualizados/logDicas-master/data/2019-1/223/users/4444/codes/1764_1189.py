s = input("Digite uma string: ")
s=s.replace(" ","")
s=s.upper()
# String vazia
inv = ""
# Contador comeca no fim da string
i = -1
while i >= -len(s):
	inv = inv + s[i]
	i = i - 1
print(s)
if(s==inv):
	print(1)
else:
	print(0)
