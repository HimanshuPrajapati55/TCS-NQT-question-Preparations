# Python code to find smallest element in an array

# Take input for the size of the array
n = int(input())  # Read the size of the array

# Take input for array elements
arr = list(map(int, input().split()))  # Read the elements of the array

# Function to find the smallest element
def find_smallest_element(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# Output the smallest element
print(find_smallest_element(arr))
