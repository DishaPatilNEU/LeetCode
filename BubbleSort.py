

# array =[67,9,77,98,89,9]
#========================= Sorting without code optimization==========================

# for i in range(0, len(array)-1):

#     for j in range(0, len(array)-1):

#         if(array[j]> array[j+1]):
#             array[j],array[j+1]=array[j+1],array[j]
          
# print(array)

#==============================Bubble sort optimized=================================



def BubbleSort(array):
    for i in range(0, len(array)-1):
        flag=0

        for j in range(0, len(array)-1):
            
            if(array[j]> array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
                flag=flag+1
        print(array)
        if(flag==0):
                print("working")
                break


array =[1,2,3,4,5]
BubbleSort(array)


