popa= int(input("qual o numero de habitantes da cidade a? "))
popb= int(input("qual o numerod e habitantes da cidade b? "))
pa= float(input("qual o percentual de crescimento da cidade a? "))
pb= float(input("qual o percentual de crescimento da cidade b? "))
cresca= (pa/100)*popa
crescb= (pb/100)*popb
anos=0
while (popa<=popb):
	popa=popa+ (pa/100)*popa
	popb= popb+(pb/100)*popb
	anos=anos+1
print(anos)