a = int(input("habitantes A: "))
b = int(input("habitantes B: "))
pa = float(input("percentual de crescimento a: "))
pb = float(input("percentual de crescimento b: "))
t = 0
while(a<b):
	a = a+a*(pa/100)
	b = b+b*(pb/100)
	t = t+1
print(t)
	
	
	
