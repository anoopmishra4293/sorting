# Python program for SelectionSort
a = [64, 25, 12, 22, 11]

for i in range(len(a)):
    min1 = i
    for j in range(i+1, len(a)): 
        if a[min1] > a[j]: 
            min1 = j 
                
    a[i], a[min1] = a[min1], a[i] 
  
print ("Sorted array",a)