st=input("insira uma sequencia de caracteres: ")
a=st.replace(" ","")
a1=a.upper()
iv=""
i=-1
while i>=-len(a):
	iv=iv +a[i]
	i=i-1
b=iv.upper()
print(a1)
if b==a1:
	print("1")
if b!=a1:
	print("0")

