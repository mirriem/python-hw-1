def sumNum(num):
    b = str(num)
    ndigits = len(b)
    sum = 0
    for i in range(ndigits):
       sum+= int(b[i])
    if sum > 9:
        sum = sumNum(sum)
    return sum
    print(sumNum(b))
    