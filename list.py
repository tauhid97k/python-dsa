"""
Given an integer array nums,
print true if any value appears at least twice in the array,
and print false if every element is distinct.
"""

# Brute force solution - Time Complexity O(n^2)
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
for i in range(len(nums)):
    # Start second loop from i+1 to skip comparing the same element
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(True)
print(False)

# Optimal Solution - Time Complexity O(n)
if len(set(nums)) == len(nums):  # Use set to remove duplicates and compare the length
    print(False)
else:
    print(True)
