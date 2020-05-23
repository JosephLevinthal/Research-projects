valor=float(input("digite o valor"))
qtickets=float(input("digite o numero"))
valordosticket=float(input("digite o numero"))
qdepasses=float(input("digite o numero"))
valordopasse=float(input("digite o numero"))
mensagem=(qtickets*valordosticket)+(qdepasses*valordopasse)
if (valor>=mensagem):
	msm="SUFICIENTE"
else:
	msm="INSUFICIENTE"
print(msm)