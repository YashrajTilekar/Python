#Addition

def Add(No1 , No2) :
    return (No1 + No2)

def main():
    print("Enter First Number")
    Value1 = int(input())

    print("Enter Second Number")
    Value2 = int(input())

    Ret = Add(Value1, Value2)
    print("Addition is :" , Ret)
    

if __name__ == "__main__" :
    main()
    