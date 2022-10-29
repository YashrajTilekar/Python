#Data : Heterogenous
#Ordered : Yes
#Indexed : Yes
#Mutable : Yes


Data = [11 , 21 , 51 , 101 ]

print("Output Using for :-")

for no in Data :
    print(no , end=" ")
print("\n--------------------------------------")

print("Output Using for With index :-")

for Cnt in range(0 , len(Data)) :
    print(Data[Cnt] , end=" ")
print("\n----------------------------------------")

print("Output Using While With Index ")
Cnt = 0
while(Cnt < len(Data)) :
    print(Data[Cnt] , end= " ")
    Cnt = Cnt + 1
print("\n------------------------------------------")