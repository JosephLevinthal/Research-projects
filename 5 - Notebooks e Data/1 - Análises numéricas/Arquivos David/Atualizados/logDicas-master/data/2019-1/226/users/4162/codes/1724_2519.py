a= int(input("insira a altura total da torre da lua: "))
s= int(input("A cada minuto, a quantidade de metros que Equecrates sobe ate o alto da Torre da Lua: "))
d= int(input("A cada minuto, a quantidade de metros que o mago Antistenes faz o guerreiro descer: "))
h=d
t=0
while h<a:
	h=h-d
	h=h+s
	t=t+1
print(t)