def Add(No1 , No2):
    return No1 + No2

AddFunction = lambda A , B : A+B

Ret1 = Add(10, 11)
Ret2 = AddFunction(10 , 11)

print("Addition Using Normal Function " ,Ret1)
print("Addition Using Lambda Function " ,Ret2)