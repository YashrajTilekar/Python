#Accept Number & Print Number of * on Screen

def Pattern(No) :
    for Cnt in range(1 , No+1 , 1):
        print("*" , end="\t")

def main() :
    print("Enter a Number")
    Value = int(input())

    Pattern(Value)

if __name__ == "__main__" :
    main()