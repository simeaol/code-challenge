from copy import deepcopy

def combinationSum(candidates, target):
        res = []
        helper(candidates, target, [], res)
        return res
        
def helper(candidates, target, buf, res):
    if target == 0:
        res.append(deepcopy(buf))
        return
    if target < 0:
        return
    for i, value in enumerate(candidates): # for i, el in enumerate(candidates)
        print(f'arr[i]={value},i={i},target={target}')
        if value > target:
             continue
        buf.append(value)
        helper(candidates, target-value, buf, res)
        buf.pop()
'''
def helper(candidates, target, start=0, buf, res):
    if target == 0:
        res.append(deepcopy(buf))
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if candidates[i] > target:
             continue
        buf.append(candidates[i])
        helper(candidates, target-candidates[i], i, buf, res)
        buf.pop()
'''
if __name__ == "__main__":
    arr = [2,4,6]
    target = 4
    result = combinationSum(arr, target)
    print("result: {}".format(result))



















''' 
==================leetCode - 39 =============
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''