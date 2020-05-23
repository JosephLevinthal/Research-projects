from numpy import*
df = array(eval(input("dias que faltou: ")))
a = 0
b = 0
c = 0
d = 0
i = 0
f = 0
n = zeros(6, dtype = float)
for e in range(size(df)):
	if(df[e] == 2):
		a = a + 1
	elif(df[e] == 3):
		b = b + 1
	elif(df[e] == 4):
		c = c + 1
	elif(df[e] == 5):
		d = d + 1
	elif(df[e] == 6):
		i = i + 1
	elif(df[e] == 7):
		f = f + 1
n[0] = round(((a/size(df)) * 100), 1)
n[1] = round(((b/size(df)) * 100), 1)
n[2] = round(((c/size(df)) * 100), 1)
n[3] = round(((d/size(df)) * 100), 1)
n[4] = round(((i/size(df)) * 100), 1)
n[5] = round(((f/size(df)) * 100), 1)
print(n)