v = input("Numero: ")
w = ""
s = len(v)

i = 0
t = 3
while i < s:
	w = w + v[i:i+3] + "."
	i = i + 3
print(w[:-1])