def Add(*Values):
    print(type(Values))
    print("Number of Arguements are : " , len(Values))

    Sum = 0
    for No in Values:
        Sum = Sum + No

    return Sum

def AddX(*Values):
    Sum = 0

    for Cnt in range(0 , len(Values) , 1):
        Sum = Sum + Values[Cnt]

    return Sum

def main():
   Ret = Add(1 , 7 , 9 , 4 , 6 , 5)
   print("Adddition is : " , Ret)

   Ret = AddX(1 , 7 , 9 , 4 , 6 , 5)
   print("Adddition is : " , Ret)

if(__name__ == "__main__"):
    main()