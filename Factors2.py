def DisplayFact(No):

    if No <= 0 :
        return

    Cnt = 1

    print("Factors are :-")
    while Cnt <= No/2 :
        if (No % Cnt) == 0 :
            print(Cnt)

        Cnt = Cnt + 1            


def main():
    print("Enter Number")
    Value = int(input())

    DisplayFact(Value)
    
##################################################
if __name__ == "__main__" :
    main()
##################################################    