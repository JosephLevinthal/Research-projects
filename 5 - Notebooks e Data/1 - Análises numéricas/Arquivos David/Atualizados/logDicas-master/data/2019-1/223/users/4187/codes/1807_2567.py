from numpy import*
Qast = int(input("quantidade de asteriscos:"))
ast = "*"
QA1 =  ast * (Qast)
t = len(QA1)

print(QA1)
for ch in range(0,len(QA1)) :
	if(Qast >= 2):
		QA1 =  ast * (Qast-1)
		print(QA1)
		Qast = Qast - 1
print(QA1)

for ch in range(0,t):
	if Qast <= (t-1) :
		QA1 = ast * (Qast + 1)
		print(QA1)
		Qast = Qast + 1
	
	
	