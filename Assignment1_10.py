#Accept Name & Display it's Length

def Length(Name) :
   return len(Name)

def main() :
    print("Enter Your Name")
    Str = input()

    Ret = Length(Str)
    print("Length is :" , Ret)

if __name__ == "__main__" :
    main()