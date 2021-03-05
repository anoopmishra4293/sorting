# Python program for insertionSort
a = [23, 23, 45, 19, 85, 35, 21, 9]

def insertion_Sort(a):
 
    for i in range(1, len(a)):
# methode 1
        for j in range(i-1,-1,-1):
            if a[j+1] < a[j]:
                a[j],a[j+1] = a[j+1],a[j]

            else:
                break

insertion_Sort(a)

print ("Sorted list is:",a)

# methode 2
        # key = a[i]
        # print("key=",key)

        # j = i-1
        # print("j=",j)
        # while j >= 0 and key < a[j] :
        #         a[j + 1] = a[j]
        #         j -= 1
        # a[j + 1] = key


# insertion_Sort(a)

# print ("Sorted list is:",a)