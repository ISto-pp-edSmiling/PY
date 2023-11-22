def fixed_sliding_window(arr: list[int], k: int) -> list[int]:
    curr_subarray = sum(arr[:k])
    result =  [curr_subarray]
    
    for i in range(1, len(arr)-k+1):
        print(i, curr_subarray)
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray + arr[i+k-1]
        
        result.append(curr_subarray)
        
    return result

print(fixed_sliding_window([1,2,3,4,5], 2))