def solve(nums):
    return recursion(nums, 0, [], [])


def recursion(nums, pos, arr, result):
    if pos == len(nums):
        result.append(arr.copy())
        return 

    else:
        recursion(nums, pos+1, arr, result)
        arr.append(nums[pos])
        recursion(nums, pos+1, arr, result)
        arr.pop() 
    return result


nums = [1,2,3]
resp = solve(nums)
print('result={}'.format(resp))


