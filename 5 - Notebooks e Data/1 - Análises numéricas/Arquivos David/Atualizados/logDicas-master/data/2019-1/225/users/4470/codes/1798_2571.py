s = input("digite: ")
sn= ""
n = len(s)
for i in  range(n):
    if(s[i] != "a") and (s[i] != "A") :
        sn = sn + s[i]
print(sn)
