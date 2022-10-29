#Accept Number & Check Whether the Number is Divisible by 5 or NOT

def Divisible5(No) :
    if((No % 5) == 0) :
        return True
    
    else :
        return False

def main() :
    print("Enter a Number")
    Value = int(input())

    Ret = False
    Ret = Divisible5(Value)

    if(Ret == True):
        print("Number is Divisible by 5")

    else:
        print("Number is NOT Divisible by 5")

if __name__ == "__main__" :
    main()