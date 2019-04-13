def sumprimes(n):
    sum1 = 0
    for i in range(0,len(n)):
        num = n[i]
        if num > 1:
            for j in range(2, int(num**0.5)+1):
                if num%j != 0:
                    sum1 = sum1 + num
        else:
            sum1 = 0
    return(sum1)