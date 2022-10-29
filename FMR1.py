def ChkEven(No):
    return((No % 2) == 0)

def Increment(No):
    return No+2

def Add(A , B):
    return A+B

def FilterX(Arr , Funcion_Name):
    Result = []

    for No in Arr:
        if(Funcion_Name(No)):
            Result.append(No)

    return Result

def MapX(Arr , Funcion_Name):
    Result = list()

    for No in Arr:
        Result.append(Funcion_Name(No))

def ReduceX(Arr):
    Sum = 0
    for No in Arr:
        Sum = Sum + No
    
    return Sum

def main():
    Data = [12 , 3 , 1 , 6 , 4 , 5 ]

    print(Data)

    Data_Filter = list(FilterX(Data, ChkEven))

    print("Data After Filter " , Data_Filter)

    Data_Map = list(MapX(Data, Increment))
    print("Data After Map " , Data_Filter)

    Ret = ReduceX(Data)
    

if(__name__ == "__main__"):
    main()