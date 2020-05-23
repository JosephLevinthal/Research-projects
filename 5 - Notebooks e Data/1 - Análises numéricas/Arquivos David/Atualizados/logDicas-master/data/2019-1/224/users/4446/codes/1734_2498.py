a= int(input("habitantes da cidade a: "))
b= int(input("habitantes da cidade b: "))
pa= float(input("percentual de crescimento a: "))
pb= float(input("percentual de crescimento b: "))
ano=0

while (a<b):
	cresca= a * pa/100
	crescb= b * pb/100
	a= a + cresca
	b= b +crescb
	ano= ano + 1
print(ano)
	
	