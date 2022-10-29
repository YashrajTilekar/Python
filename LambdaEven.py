def ChkEven(No):
    if(No % 2  == 0):
        return True
    else:
        return False

def ChkEvenX(No):
    return ((No % 2) == 0)

Ret = ChkEven(12)

if(Ret == True):
    print("It's Even")
else:
    print("It's Odd")

Ret = ChkEvenX(12)

if(Ret == True):
    print("It's Even")
else:
    print("It's Odd")

EvenOdd = lambda No : ((No % 2) == 0)
Ret = EvenOdd(12)

if(Ret == True):
    print("It's Even")
else:
    print("It's Odd")