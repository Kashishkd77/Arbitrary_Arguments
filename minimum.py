# find the minimum among n numbers passed as input in a function
# keyword argument concept used
def minimum(*n):
    # if min=n then the entire values passed in the function gets printed
    small = 0
    #for i in range(n):
    for i in n:
        if small==0 :
            small = i
        else:
            if small > i :
                small = i
    print("The minimum among all the numbers is :",small)
minimum(-99,11,23,11,-898,14,78,2,0,-1)