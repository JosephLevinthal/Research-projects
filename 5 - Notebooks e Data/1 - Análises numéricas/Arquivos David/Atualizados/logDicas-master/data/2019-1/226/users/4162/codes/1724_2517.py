h0= float(input("insira a altura inicial do objeto: "))
t=0
h=h0-(9.8*(t**2))/2
while h>0:
	print("t =",round(t,1))
	print("h =",round(h,1))
	t=t+1
	h=h0-(9.8*(t**2))/2



