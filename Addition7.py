from sys import *

def Add(A , B) :
    Ans = 0
    Ans = A + B

    return Ans

def main():
    print("Welcome to : " ,argv[0])

    if(len(argv) == 1):
        if(argv[1] == "--U"):
            print("Use the application as : ")
            print("python Name_Of_Application First_Number Second_Number")
            exit()

        if(argv[1] == "--H"):
            print("Help: This Application is Used to perform addition of two Numbers ")
            exit()
    

    if(len(argv) != 3) :
        print("Invalid Number of Arguements ")
        print("Use --U flag to get Usage")
        exit()

    Ret = Add(int(argv[1]), int(argv[2]))
    print("Addition is : " ,Ret)
    
#Starter
if __name__ == "__main__" :
    main()
    