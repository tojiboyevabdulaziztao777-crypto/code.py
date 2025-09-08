f=open("a.txt",encoding="utf-8")

sit=set('0123456789')
count=0

for x in f.read().split("\n"):
        a = x.split(',')
        if set(a[0]) == sit:
            print(sit)
            print(set(a[0]))
            print(a[-1])
            print(a[-2])
            print(a[-4],"\n")
            count+=1

print(count)
f.close()

# tushunmadim