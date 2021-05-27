def factorial(*n):
    for i in n:
        fact = 1
        for j in range(1,i+1):
            fact=int(fact*j)
        print("The factorial of ",i," --> ",fact)
factorial(2,4,5,78,90,1,0,8,7)