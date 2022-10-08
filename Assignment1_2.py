#EvenOdd

def ChkNum(Number) :
    
    if((Number % 2) == 0) :
        print("Even Number")

    else :
        print("Odd Number")


def main():
    print("Enter a Number")
    Value = int(input())

    ChkNum(Value)
    

if __name__ == "__main__" :
    main()
    