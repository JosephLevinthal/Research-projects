a = int(input("num de habitantes de A: ")) 
b = int(input("num de habitantes de B: "))
percenta = float(input("percentual de crescimento populacional de A: "))
percentb = float(input("percentual de crescimento populacional de B: "))
ab = a - b 
aa = 0
ba = 0 
cont = 0


while(a < b):
	hab1 = a*(percenta/100)
	a = a + hab1
	
	hab2 = b*(percentb/100)
	b = b + hab2
	cont = cont + 1
	
print(cont)

