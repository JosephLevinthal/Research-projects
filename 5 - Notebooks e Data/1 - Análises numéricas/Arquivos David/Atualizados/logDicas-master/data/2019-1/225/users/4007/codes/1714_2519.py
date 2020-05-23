a = int(input("altura da torre: "))
s = int(input("altura que consegue subir/minuto: "))
d = int(input("mago faz descer/minuto: "))
i = 0
c = 0
while (c != a) or (c > a):
	c = (c + s) - d
	
	if (c != a):
		
		print(i)
	
	i = i + 1
