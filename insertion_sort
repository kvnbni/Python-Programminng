
# Insertion Sort
#a is an array
def insertion_sort(a):
    length_of_array=len(a)
    for i in range(1,length_of_array):  # i to loop over unsorted portion
        element_in_unsorted_portion=a[i]
        j=i  # j to loop over the sorted portion 
        while j>0 and a[j-1]>element_in_unsorted_portion:
            a[j]=a[j-1]
            j=j-1
            # loop exits with the value of j where the unsorted element should be inserted
        a[j]=element_in_unsorted_portion
    
        print 'Array after step {}'.format(i)
        # printing the sorted array after each step
        for i in range(0,length_of_array):
            print(a[i]),    # To print the entire array in the same line
        print '\n'
        
        
#Calling the function
a=[6,5,4,3,2,1]        
insertion_sort(a)
    
        
        
        
