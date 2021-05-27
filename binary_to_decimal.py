def binary(*n):
    for i in n:
        y=x=i
        count=0
        while x!=0:
            x=x//10
            count=count+1
        j=0
        decimal=0
        while y!=0:
            rem=y%10
            decimal=decimal+rem*pow(2,j)
            y=y//10
            j=j+1
        print("The decimal form of ",i," --> ",decimal)
binary(101,11,101011)