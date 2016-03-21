def insert_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]<key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
array = [1, 5, 4, 6, 3, 2, 7]
# print type(len(array))
array2 = insert_sort(array)
print array2
insert_sort(array)
for a in array:
    print a,
