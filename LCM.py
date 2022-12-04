def compute_lcm(x,y):
    if x > y :
        greater = x
    else:
            greater = y
    while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
    return lcm
num1 = int(input("num1: "))
num2 = int(input("num2: "))
print("The L.C.M. is a ", compute_lcm (num1,num2))
