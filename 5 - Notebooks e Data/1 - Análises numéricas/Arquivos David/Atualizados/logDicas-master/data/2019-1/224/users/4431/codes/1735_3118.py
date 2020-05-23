x=float(input("digite um numero: "))
while(x>=0):
	if(x>=0):
		a=(x//1000000000)%10
		b=(x//100000000)%10
		c=(x//10000000)%10
		d=(x//1000000)%10
		q=(x//100000)%10
		w=(x//10000)%10
		h=(x//1000)%10
		v=(x//100)%10
		t=(x//10)%10
		p=(x%10)
		if(x>=0)and(x<=9):
			n=1
		elif(x>=10)and(x<=99):
			n=2
		elif(x>=100)and(x<=999):
			n=3
		elif(x>=1000)and(x<=9999):
			n=4
		elif(x>=10000)and(x<=99999):
			n=5
		elif(x>=100000)and(x<=999999):
			n=6
		elif(x>=1000000)and(x<=9999999):
			n=7
		elif(x>=10000000)and(x<=99999999):
			n=8
		elif(x>=100000000)and(x<=999999999):
			n=9
		elif(x>=1000000000)and(x<=9999999999):
			n=10								
		a=a**n
		b=b**n
		c=c**n
		d=d**n
		q=q**n
		w=w**n
		h=h**n
		v=v**n
		t=t**n
		p=p**n
		m=a+b+c+d+q+w+h+v+t+p
		if(m==x):
			print("ARMSTRONG")
			x=float(input("Digite um numero: "))
		else:
			print("NAO ARMSTRONG")
			x=float(input("Digite um numero: "))


	 
  

		