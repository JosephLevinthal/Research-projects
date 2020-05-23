from numpy import*
v = array(eval(input("saques: ")))
i = 0
s = 0
while(i < size(v)):
	if (v[i] <= 50):
		s = s + 1
	i = i + 1
print(s)
i = 0
t = []
while (i < size(v)):
	if(v[i] <= 50):
		i = i
		t.append(i)
	i = i + 1
print(str(t).replace(',',''))



		