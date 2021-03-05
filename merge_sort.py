# Python program for MergeSort
a = [19, 56, 59, 26, 34, 12, 3, 97]

def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2

        l = a[:mid]
        r = a[mid:]

        mergeSort(l)

        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1
        
mergeSort(a)
print("Sorted list is: ",a)

