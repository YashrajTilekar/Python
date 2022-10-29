#Accept Number & Print First 10 Even Numbers

def Pattern() :
    No = 1  
    Cnt = 0
    
    while(Cnt != 10) :
        if((No % 2) == 0) :
            print(No , end="\t")
            Cnt = Cnt + 1
        
        No = No + 1


def main() :
    #print("Enter a Number")
    #Value = int(input())

    Pattern()

if __name__ == "__main__" :
    main()