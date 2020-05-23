a = int(input("insira um numero: "))
b = ""
c = a
while c > 0 :
	b = c * "*"
	c = c - 1
	print(b)
for i in range(a + 1):
	print(i *"*")
