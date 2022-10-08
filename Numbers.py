def DisplayFact(No):

    if No <= 0 :
        return

    Cnt = 1

    print("Factors are :-")
    while Cnt <= No/2 :
        if (No % Cnt) == 0 :
            print(Cnt)

        Cnt = Cnt + 1            

def Add(No1 , No2) :
    return (No1 + No2)