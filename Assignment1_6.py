#Accept Number & Check Whether the Number is +ve , -ve or 0

def NumberValue(No) :
    if(No > 0) :
        print("Positive Number")

    elif(No < 0) :
        print("Negative Number")
    
    elif(No == 0) :
        print("Zero")




def main() :
    print("Enter a Number")
    Value = int(input())

    NumberValue(Value)

if __name__ == "__main__" :
    main()