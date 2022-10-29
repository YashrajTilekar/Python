print("Demonstration of Set")

# Data : Heterogenous
# Ordered : No
# Indexed : No
# Mutable : Yes  #####################
# Duplicates : No


Data = {11 , 21 , 51 , 101 , 11}
Data1 = {11 , 76.77 , True , "Hello"}  # Heterogenous

print("First Set Data" , Data)
print(len(Data))
print("Data is Heterogenous :" , Data1)
print("Data is Not Ordered :" , Data1)

print("Set is Mutable")
Data.add(211)

print("Data after insertion :" , Data)

Data.discard(201)
print("Data after Removal :" , Data)

