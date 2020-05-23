valor = int(input("tem quantos malandro?  "))     #valor que ele tem disponivel
qdt = int(input("quantos quer?  "))       #quant. de tichets do ru que ele quer comprar
vt = float(input("qual preco?  "))        #valor dos tickets
qpso = int(input("quantos tem?  "))      #quantidade de passes de onibus
vdp = float(input("qual preco?  "))       #valor dos passes

x =(qdt * vt) + (qpso * vdp)

if(valor >= x):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"
print(msg)