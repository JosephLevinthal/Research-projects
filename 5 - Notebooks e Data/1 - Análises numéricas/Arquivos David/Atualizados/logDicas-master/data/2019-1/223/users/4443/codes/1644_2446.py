#Coleta da senha do usuario
senha = int(input("Digite uma senha com 6 digitos: "))

#Separacao dos numeros por posicao
p = senha//100000
rp = senha%100000
s = rp//10000
rs = rp % 10000
t = rs//1000
rt = rs%1000
q = rt//100
rq = rt%100
qui = rq//10
sex = rq%10
#Soma das posicoes pares
par = s + q + sex
impar = p + t + qui
#verificacao da senha
if(par%impar == 0):
			print("acesso liberado")
else:
	print("senha invalida")