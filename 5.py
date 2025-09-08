f=open("b.txt",encoding="utf-8")
z=dict()

for i in f.read().split("\n"):
    u=i.split(",")
    if u[4] not in z:
        z[u[4]] = 1
    else:
        z[u[4]] += 1

print(z)

a=max(z.values())

for k,v in z.items():
    if v==a:
        x=k

print(x)

f.close()
