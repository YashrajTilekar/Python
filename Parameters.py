#Positional Arguements
def Add1(No1 , No2):
    print("Value of No1 :",No1)
    print("Value of No2 :",No2)

    return No1 + No2

def Sub1(No1 , No2):
    print("Value of No1 :",No1)
    print("Value of No2 :",No2)

    return No1 - No2

def main():
    Ret = 0
    Ret = Add1(10, 11)
    print("Addition is : ", Ret)

    Ret = Sub1(No2 = 20, No1 = 10)
    print("Subtraction is : " , Ret)

if(__name__ == "__main__"):
    main()