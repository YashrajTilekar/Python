print("Demonstration of Dictionary")

# Data : Heterogenous
# Ordered : Yes
# Indexed : NO
# Mutable : Yes  #####################
# Duplicates : Key - NO , Value - Yes

Batches = {"PPA" : 18000 , "LB" : 16700 , "Python" : 16500 , "Angular" : 15000}

print("Data of Dictionary :" , Batches)

print("Data Traversal Using for Loop :")
for X in Batches :
    print(X)


print("Data Traversal Using for Loop :")
for X in Batches :
    print(X , Batches[X])


print("Data Traversal Using for Loop :")
for X in Batches :
    print(X , Batches.get(X))


keyBatches = list(Batches.keys())
print(keyBatches)
print(type(keyBatches))

valueBatches = list(Batches.values())
print(type(valueBatches))
print(valueBatches)

for Cnt in range(0 , len(Batches)) :
    print("Batch Name is : ", keyBatches[Cnt] , end=" ")
    print("Fees Are : " ,valueBatches[Cnt])
