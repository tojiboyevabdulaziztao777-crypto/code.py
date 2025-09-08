# import lib as z
# ===============================================================================================================

def Teskari(a:str):
    return a[::-1]

# -------------------------------------------

def Kun(a:str):
    if a[0:1]=="0":
        print(a[1:2],"-",end="")
    else:
        print(a[:2],"-",end="")
    
    if a[3:5]=="01":
        print(" yanvar ",end="")
    elif a[3:5]=="02":
        print(" fevral ",end="")
    elif a[3:5]=="03":
        print(" mart ",end="")
    elif a[3:5]=="04":
        print(" aprel ",end="")
    elif a[3:5]=="05":
        print(" may ",end="")
    elif a[3:5]=="06":
        print(" iyun ",end="")
    elif a[3:5]=="07":
        print(" iyul ",end="")
    elif a[3:5]=="08":
        print(" avgust ",end="")
    elif a[3:5]=="09":
        print(" sentiyabr ",end="")
    elif a[3:5]=="10":
        print(" oktiyabr ",end="")
    elif a[3:5]=="11":
        print(" noyabr ",end="")
    elif a[3:5]=="12":
        print(" dekabr ",end="")
    
    print(",",a[6:10],"- yil")

# ---------------------------------------------

def DA():
    r=float(input("radius kiriting : "))
    a=r*2*3.1416
    print("aylananing uzunligi : ",a)
    b=r*r*3.1416
    print("aylananing yuzi : ",b)

# -------------------------------------------------

def InputDict():
    lst=[]
    uzunlik=int(input("nechta dict kiritasiz : "))
    for i in range(uzunlik):
        a=input("key kiriting : ")
        b=input("value kiriting : ")
        a={a:b}
        lst.append(a)
    return lst

# ===============================================================================================================

if __name__=="__main__":
    ...

# ===============================================================================================================
