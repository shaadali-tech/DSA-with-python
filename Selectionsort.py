# def selectionsort(arr):

#   n=len(arr)

#   for i in range (n):
#     min=i
#     for j in range(i,n):
#       if arr[min]>arr[j]:
#         min=j
#     arr[i],arr[min]=arr[min],arr[i]

# arr=[5,6,3,1,6,6,10]
# selectionsort(arr)
# print(arr)

# Selection Sort Algorithm

# def SelectionSort(arr):

#   n=len(arr)
#   for i in range(n):
#     min_index=i
#     for j in range(i,n):
#       if arr[j]<arr[min_index]:
#         min_index=j
#     arr[i],arr[min_index]=arr[min_index],arr[i]




# BUBBLE SORT PROGRAM

# arr=[2,5,4,7,1,3,6]
# n=len(arr)
# for i in range(n-2,-1,-1):
#   for j in range(0,i+1):
#     if arr[j]>arr[j+1]:
#       arr[j],arr[j+1]=arr[j+1],arr[j]

# print(arr)

# INSERTION SORT

# def InsertionSort(arr):
#   n=len(arr)
#   for i in range(1,n):
#     key=arr[i]
#     j=i-1
#     while(j>=0 and key<arr[j]):
#       arr[j+1]=arr[j]
#       j=j-1
#     arr[j+1]=key


# arr=[5,6,3,1,6,6,10]
# InsertionSort(arr)
# print(arr)

# MERGE SORT

def merge_array(left, right):
    n = len(left)
    m = len(right)

    result = []

    i, j = 0, 0

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_array(left, right)


arr = [8, 3, 5, 1, 9, 6, 2]

print(merge_sort(arr))