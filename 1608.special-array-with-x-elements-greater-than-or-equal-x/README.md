# 1608. Special Array With X Elements Greater Than or Equal X

## Solution:

# Brute force

Space O(1)
Time O(N^2)

Loop from 0 to length of nums, count the number satisfy the condition.

# Sort and scan

Space O(1)
Time O(N lgN)  [O(N lgN) for sorting and O(N) for scanning]

Sort nums from larger to smaller. Find the x left-most nums which greater than x.
* If nums[x+1] is less than x, means exactly x nums greater than x (result)
* If nums[x+1] equals to x, means at least x+1 nums greater than or equal to x (-1)

# Sort and binary search

Space O(1)
Time O(N lgN)  [O(N lgN) for sorting and O(lgN) for binary search]

Refinement for previous solution. Use binary search to find x left-most nums wich greater than x.