t = int(input("tempo de investimento em meses"))
Qf=1042000
Qo=1500
i=(((Qf/Qo)**(1/t))-1)
if (i<=0.01):
 a = "Real"
else:
 a = "Irreal"
print(round(i,5))
print(a)
