def prime(*n):
    for i in n:
        if(i>1):
            flag = 0
            for j in range(2,i):
                if i%j==0:
                    flag=1
                    break;
            if flag==1:
                print(i," --> not prime number")
            else:
                print(i, " --> prime number")
        else:
            print(i, " --> not prime number")
prime(10,9,45,6,7,2,1,0,88,3,-1)