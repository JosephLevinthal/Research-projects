i= int(input("qual sua idade?: "))
if i>=18:
	msg="eleitor"
if i<18:
	msg="nao_eleitor"
print(msg.lower())
