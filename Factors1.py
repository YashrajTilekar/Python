def DisplayFact(No):

    if No <= 0 :
        return
        
    for Cnt in range(1 , int((No/2)) + 1 , 1):
        if (No % Cnt) == 0 :
            print(Cnt)


def main():
    print("Enter Number")
    Value = int(input())

    DisplayFact(Value)
    
##################################################
if __name__ == "__main__" :
    main()
##################################################    