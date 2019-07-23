cords1 = raw_input("1st pair (x1 y1 x2 y2) ")
cords2 = raw_input("2nd pair (x3 y3 x4 y4) ")
dif1 = int(cords1[4]) - int(cords2[0])
dif2 = int(cords1[6]) - int(cords2[2])
if dif1 < dif2 == True :
    result = dif2 * dif2
    print('Farmer John needs a pen of an area of ', result)
elif dif1 > dif2 == True :
    result = dif1 * dif1
    print('Farmer John needs a pen of an area of ', result)
else :
    result = dif1 * dif1
    print('Farmer John needs a pen of an area of ', result)
