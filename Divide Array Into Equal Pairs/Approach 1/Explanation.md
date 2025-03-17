# Approach 2: Map


## Algorithm
- Create a frequency map frequency to store the count of each number in nums.
- For each number num in the array nums:
    - If num already exists in frequency, increment its count by 1.
    - Else, add it with a count of 1.
- For each unique number num in the frequency map:
    - Get the count of this number from frequency.
    - If the count is not divisible by 2, return false since we cannot pair all occurrences.
- If we checked all numbers without finding any odd frequencies, return true.