

array =[67,77,98,89,3,9]

for i in range(0, len(array)-1):
    min = array[i]
    for j in range(i+1, len(array)):

        if(array[j]< min):
            array[i],array[j]=array[j],array[i]
            min= array[i]
print(array)
        


