a1, b1, f1, k1 = map(int, input().split())
counter1 = 0
b21 = b1-f1
if (b21 >= 0):
    di1 = (a1-f1)*2
    for i in range (k1):
        if (i == k1-1):
             di1 =di1/ 2
        if (b21 < di1):
            b21 = b1
            counter1 += 1
        b21 = b21 - di1
        if (b21 < 0):
            counter1 = -1
            break
        di1 = 2*a1 - di1

    print (counter1)
else:
    print (-1)
