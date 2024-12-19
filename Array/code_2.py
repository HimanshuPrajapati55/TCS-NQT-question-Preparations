n = int(input())
arr = list(map(int, input().split()))

def largest_element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
           largest = num
    return largest

print(largest_element(arr))