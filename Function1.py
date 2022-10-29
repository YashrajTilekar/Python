#Function Which Accepts Nothing And Returns Nothing
def Demo1():
    print("Inside Demo1")

#Function Accepts One Parameter and Returns Nothing
def Demo2(No):
    print("Inside Demo2 With One Arguement : ",No)

#Function Accepts One Parameter and Returns One Parameter
def Demo3(No):
    print("Inside Demo3 with Arguement : " , No) 
    return No+2

#Function Accepts Two Parameter and Returns One Parameter
def Demo4(No1 , No2):
    print("Inside Demo4")
    Add = No1 + No2

    return Add

def Demo5(No1 , No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2

    return Add , Sub

def main():
    Demo1()
    Demo2(11)

    Ret = Demo3(21)
    print("Return Value of Demo3 is : " , Ret)

    Ret = Demo4(11, 21)
    print("Return Value of Demo4 is : " ,Ret)

    Ret1 , Ret2 = Demo5(11, 10)
    print("First Return Value : " , Ret1)
    print("Second Return Value : " , Ret2)

if(__name__ == "__main__"):
    main()