f=open("a.txt",encoding="utf-8")
lst=[]
sit=set()
for x in f.read().split("\n"):
    u=x.split(',')
    if u[1]=="visa":
        lst.append(u[-1])
for i in lst:
    sit.add(i)
print(f"{sit}")

f.close()