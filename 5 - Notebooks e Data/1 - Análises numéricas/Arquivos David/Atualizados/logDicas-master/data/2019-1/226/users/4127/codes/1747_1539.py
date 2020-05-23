x= float(input("qual seu numero x?"))
k= int(input("qual seu termo geral? "))
t=0
s=0

while(t<k):
	s=s+ (x**t)*((-1)**t)
	t=t+1
print(round(s,7)
	  )
