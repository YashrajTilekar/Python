def Area(Radius , Pi = 3.14159265359):
    Result = Pi * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PiValue = 3.14

    Ret = Area(RValue , PiValue)
    print("Area of Circle is : " , Ret)   

    Ret = Area(10.5)
    print("Area of Circle is : " , Ret)

    Ret = Area(Radius= 10.5 )
    print("Area of Circle is : " , Ret)
    

if(__name__ == "__main__"):
    main()