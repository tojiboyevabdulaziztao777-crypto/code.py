lugat={
    "English" : {},
    "Spanish" : {},
    "French"  : {}
}

for i in range(10):
    til=input(">>> ")
    if til in lugat:
        soz=input(f"{til}: ")
        if soz not in lugat[til]:
            lugat[til][soz]=input("Uzb: ")
    else: 
        lugat[til]={}
        a=input(f"{til}: ")
        b=input("UZB: ")
        lugat[til][a]=b

print(lugat)