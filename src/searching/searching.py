# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1
        
    mid = (start + end) // 2

    if target is arr[mid]:
        return mid 

    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)

    return binary_search(arr, target, mid + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def descending_binary_search(arr, target, left, right):
    # base case 
    # or we searched the whole array, i.e. when left > right
    if left > right:
        return -1
    # how do we move closer to a base case? 
    # we'll stop when we either find the target 
    else:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            # rule out the right side
            return descending_binary_search(arr, target, left, mid - 1)
        else:
            # rule out the left side 
            return descending_binary_search(arr, target, mid + 1, right)


def agnostic_binary_search(arr, target):
    # Your code here
    # figure out whether the input array is sorted in ascending or descending order 
    # keep a boolean to indicate the order of the array 
    # compare arr[0] and arr[1] 
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    # if the input array is ascending, call `binary_search` with the array and target 
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # otherwise, call `descending_binary_search` with the array and target 
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)
    
    
    
    
    
    # def binary_search(arr, target, start, end):  
    # # start = 0
    # # end = n - 1
    # # Base condition (search space is exhausted)
    # if start > end:
    #     return - 1
    
    # # we find the mid space in the search space and compares it with key value
    # mid = (start + end) // 2
    
    
    # # Compare target with the middle element 
    # # Base condition (key value is found)
    # if target == arr[mid]:
    #     # If target matches with the middle element, return the mid index
    #     return mid
    
    #         # if target value is smaller than the middle element in the array,
    # elif target < arr[mid]:
    #     # discard all elements in the right search space including the mid element i.e. arr[mid...high]
    #     return binary_search(arr, start, mid - 1, target)
    #     # now our new hgh would be mid - 1
        
    # else: # if target value is greater than the middle element in the array,
    #     # discard all elements in the left search space including the mid element i.e. arr[low...mid]
    #     return binary_search(arr, mid + 1, end, target)
    #     # now our new low would be mid + 1
    # # Repeat the process until target is found or the search space is exhausted