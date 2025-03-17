# Approach 3: Boolean Array

## Algorithm
- Initialize a variable maxNum to store the largest value in the array nums.
- For each number num in nums:
    - Update maxNum if num is larger than the current maxNum.
- Create a boolean array needsPair of size maxNum + 1 to track pairing status.
- For each number num in nums:
    - Toggle the value at needsPair[num] from true to false or false to true.
- For each number num in nums:
    - Check if needsPair[num] is true.
    - If true, it means this number appeared an odd number of times, so return false.
- If no unpaired numbers are found, return true.