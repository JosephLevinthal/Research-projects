qpt=int(input("quantidade de pergaminhos na torre: "))
qvt=int(input("quantidade de varinhas na torre: "))
pcp=float(input("percentual de crescimento do pergaminho: "))
pcv=float(input("percentual de crescimento da varinha: "))

sp=0
sv=0
i=0

while(sp+sv<80000):
	crescp= qpt * pcp/100
	crescv= qvt * pcv/100
	sp= sp + qpt + crescp
	sv= sv + qvt + crescv
	i= i + 1
print(i)