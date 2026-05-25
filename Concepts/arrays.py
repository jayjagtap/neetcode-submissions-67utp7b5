nums = [[1,1,1,1,2,2,2,3,4], [1,1,2,3], [1,2,3,4,5,6]]

def sorted_list_sequence(nums):
    
    size = len(nums)
    if size == 0: return 1

    i, j = 0, 1

    while j < size:
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
        j+=1
    
    return nums, i+1
 

nums, unique = sorted_list_sequence([1,2,3,4,5,6])
print(unique)


# Prefix Sum 
arr = [1, -2, 3, 4, -1]

def build_prefix_sum(arr):
    prefix_sum = [0]

    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)

    return prefix_sum

prefix_sum = build_prefix_sum(arr)

# sum from index i to j
i = 2
j = 4
print(prefix_sum[j+1] - prefix_sum[i])


# Kadane's algorithm

def kadanes_algo(nums):

    current = nums[0]
    best = nums[0]
    temp_start, temp_end = 0, 0
    best_start, best_end = 0, 0

    for i in range(1, len(nums)):
        if current + nums[i] < nums[i]: # new start
            temp_start, temp_end = i , i
            current = nums[i]
        else:
            temp_end = i
            current += nums[i]
            
        if current > best:
            best_start, best_end = temp_start, temp_end
            best = current

    return best, best_start, best_end

print("Kadanes")
print(kadanes_algo([5, -9, 6, -2, 3]))