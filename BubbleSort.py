def bubbleSort(array):

 for i in range(len(array)):
       # loop to compare array elements
       for j in range(0, len(array) - i - 1):
           # compare two adjacent elements
           # change > to < to sort in descending order
           array_j = array[j]
           array_j_1 = array[j+1]
           if array[j] > array[j + 1]:
               # swapping elements if elements
               # are not in the intended order
               temp = array[j]
               array[j] = array[j + 1]
               array[j + 1] = temp

def bubbleSortdescending(array):
 for i in range(len(array)):
       # loop to compare array elements
       for j in range(0, len(array) - i - 1):
           # compare two adjacent elements
           # change > to < to sort in descending order
           array_j = array[j]
           array_j_1 = array[j+1]
           if array[j] < array[j + 1]:
               # swapping elements if elements
               # are not in the intended order
               temp = array[j]
               array[j] = array[j + 1]
               array[j + 1] = temp

def find_min(array):
    min= array[0]
    #print(max)
    for i in range(0,len(array)-1):
        if array[i+1]<min:
            min = array[i+1]

    print('min no from(',data1,') is: ',min)

def find_max(array):
    max= array[0]
    #print(max)
    for i in range(0,len(array)-1):
        if array[i+1]>max:
            max = array[i+1]

    print('max no from(',array,') is: ',max)

def find_average(array):
    sum_data=0
    for i in range(0,len(array)):
        sum_data=sum_data+array[i]
    print(sum_data)
    print('average no from(',array,') is: ',sum_data/len(array))

def find_average2(array1,array2):
    sum_data=0
    for i in range(0,len(array1)):
        sum_data=sum_data+(array1)[i]
    print(sum_data)

    for j in range(0,len(array2)):
        sum_data=sum_data+(array2)[j]
    print(sum_data)
    print('average no from(',array1,array2,') is: ',sum_data/len(array1+array2))

array=[1,2,5,4,6,7]
number=7
def just_find(array,number):
    array_no=0
    array_index=0
    for i in range(len(array)):
        if array[i]==number:
            array_no=array[i]
            array_index=i
            break

    if array_no == number:
        print("number ",number," found at index ",array_index,":)")
    else:
        print("not found :(")







data1 = [5,8,7,2,4,3,1]
data2 = [13,5,11,6]
find_min(data1)
find_max(data1)
find_average2(data1,data2)
just_find(array,number)
#print('python sort: ',sorted([8,5,7,2,4,3,1],reverse=1))
#bubbleSort(data)


#print('Sorted Array in Ascending Order:')
#print(data)

#print('Sorted Array in descending Order:',sorted([8,5,7,2,4,3,1]))
#bubbleSortdescending(data)
#print(data)

#print('Sorted Array in descending Order:')
#print(data)