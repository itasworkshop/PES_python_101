
mytuple = (1,2,43,5,6,7,96,3)

templist1 = []
templist2 = []

for i in mytuple:
    if i%2==0:
        templist1.append(i)
    else:
        templist2.append(i)


result1 = tuple(templist1)
result2 = tuple(templist2)

print(result1)
print(result2)
