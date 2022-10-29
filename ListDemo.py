print("Demonstration of List")

#Data : Heterogenous
#Ordered : Yes
#Indexed : Yes
#Mutable : Yes


Data = [11 , 21 , 51 , 101 , 11]
Data1 = [11 , 76.77 , True , "Hello"]  # Heterogenous

print("Data is Heterogenous :" , Data1)
print("Data is Ordered :" , Data1)
print("Data at Index 2 : ", Data1[2])
print("Data With Duplicate elements :",Data)

print("List is mutable")
Data.append(201)
print("Data After Append" , Data)

Data.pop()
print("Data After Pop" , Data)