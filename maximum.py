# finding maximum no. among n passed numbers in a funtion i.e. usig keyword arguments
def maximum(*n):
    large=0
    for i in n:
        if large==0:
            large=i
        else:
            if large < i:
                large = i
    print("The maximum among all the numbers is :",large)
maximum(1222,89,3,578,0,278,7,88,3,1,11111,11)