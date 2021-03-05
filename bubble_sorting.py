# Python program for bubbleSort
a = [19, 54, 25, 96, 4, 32, 15, 2] 

def bubble_Sort(a): 
    x = len(a) 
    
    for i in range(x): 
        
        for j in range(0, x-i-1): 

            if a[j] > a[j+1] : 
                a[j], a[j+1] = a[j+1], a[j] 
  
bubble_Sort(a)  
print ("Sorted list is:",a) 