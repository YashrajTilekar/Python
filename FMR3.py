from functools import reduce

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

    Data_Filter = list(filter(lambda No:((No % 2) == 0) , Data_Input))

    print("Data After Filter is  : " , Data_Filter)

    Data_Map = list(map(lambda No : No * 2 , Data_Filter))
    print("Data After Mapping : " , Data_Map)

    Data_Reduce = reduce(lambda A , B : A + B , Data_Map)
    print("Data after Reduce :",Data_Reduce)

if(__name__ == "__main__"):
    main()