temp= input("qual a escala de temperatura? (C ou F)")
valtemp= float(input("qual a temperatura?"))

c= (5/9)*(valtemp-32)
f= (valtemp*(9/5))+32

if (temp.upper()=="F"):
	msg= c
if (temp.upper()=="C"):
	msg=f
print(msg)