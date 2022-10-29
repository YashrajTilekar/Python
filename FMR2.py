def CheckEven(No):
    return ((No % 2) == 0)

def Doubles(No):
    return No * 2

def Sum(A , B):
    return A+B

def FilterX(Helper_Function , Data):
    Result = list()

    for No in Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    
    return Result

def MapX(Helper_Function , Data):
    Result = list()

    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    
    return Result

def ReduceX(Helper_Function , Data):
    Ans = 0
    for No in Data:
        Ans = Helper_Function(Ans , No)
    
    return Ans

def main():
    print("Enter Number of Elements you want to Enter :- ")
    Size = 0
    Size = int(input())

    Data_Input = list()

    print("Enter the Elements")
    for Cnt in range(0 , Size , 1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :- \n" ,Data_Input)

    Data_Filter = FilterX(CheckEven , Data_Input)

    print("Data After Filter is  : " , Data_Filter)

    Data_Map = MapX(Doubles , Data_Filter)
    print("Data After Mapping : " , Data_Map)

    Data_Reduce = ReduceX(Sum, Data_Map)
    print("Data after Reduce :",Data_Reduce)

if(__name__ == "__main__"):
    main()