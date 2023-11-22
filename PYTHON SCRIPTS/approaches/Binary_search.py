# https://www.youtube.com/watch?v=fDKIpRe8GW4
# this only works for a sorted array.
# to find value in sorted array:

def binary(array, target):
    left,right = 0, len(array)-1
    
    while (left <= right):
        mid = (right + left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1           # return if target not in array

print(binary([1,2,6,7,26,43], 26))