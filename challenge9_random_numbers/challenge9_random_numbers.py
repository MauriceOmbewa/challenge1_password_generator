# Importing necessary modules
import random
import time

# Defining the function to perform quicksort
def quicksort(arr):
    # Base case - if there is only 1 or 0 elements in the array, return it as is
    if len(arr) <= 1:
        return arr
    
    # Selecting a pivot element to split the array
    pivot = arr[len(arr) // 2]
    
    # Splitting the array into three sub-arrays based on the pivot element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sorting the left and right sub-arrays and combining them with the middle array
    return quicksort(left) + middle + quicksort(right)

# Generating an array of random integers
n = 1000  # Number of random numbers
numbers = [random.randint(1, 1000) for _ in range(n)]

# Sorting the array using quicksort and measuring the execution time
start_time = time.time()  # Start the timer
sorted_numbers = quicksort(numbers)  # Call the quicksort function
end_time = time.time()  # Stop the timer
execution_time = end_time - start_time  # Calculate the execution time

# Printing the original array, sorted array and execution time
print("Original numbers:", numbers)
print("Sorted numbers:", sorted_numbers)
print("Time taken to sort:", execution_time, "seconds")
