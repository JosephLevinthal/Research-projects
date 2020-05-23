j=int(input("Digite o numero com dois digitos: "))
l=int(input("Digite o numero sorteado na loteria: "))

jd=j//10
ju=j%10
ld=l//10
lu=l%10

if(j==l):
	print("Ganhou R$ 100.000,00")
elif(jd==lu and ju==ld):
	print("Ganhou R$ 50.000,00")
elif((jd==ld and ju!=lu) or (jd==lu and ju!=ld) or (ju==ld and jd!=lu) or (ju==lu and jd!=ld)):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")


	