# Explanation of the Solution for Canvas 2094 - Finding 3-Digit Even Numbers

## Code Overview

```python
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        digitHashmap = Counter(digits)
        for i in range(100,1000,2):
            numberHashmap = Counter([int(j) for j in str(i)])
            flag = 0
            for k in numberHashmap.keys():
                if numberHashmap[k] > digitHashmap[k]:
                    flag = 1
            if flag == 0:
                ans.append(i)
        return ans
```

## Step-by-Step Explanation

### Step 1: Import Counter

This code assumes `Counter` is imported from the `collections` module.

```python
from collections import Counter
```

### Step 2: Count the Available Digits

```python
digitHashmap = Counter(digits)
```

This line creates a frequency map (`digitHashmap`) that stores how many times each digit appears in the input list.

For example, if `digits = [2, 2, 8, 8, 2]`, then:

```python
digitHashmap = {2: 3, 8: 2}
```

### Step 3: Loop Through All 3-Digit Even Numbers

```python
for i in range(100, 1000, 2):
```

This loop goes from 100 to 999, skipping every odd number (since we increment by 2), effectively checking **only even numbers**.

### Step 4: Create a Frequency Map of Each Number's Digits

```python
numberHashmap = Counter([int(j) for j in str(i)])
```

This line converts a number (like 228) into a list of its digits `[2, 2, 8]`, and counts how many times each digit occurs in it.

For `i = 228`, we get:

```python
numberHashmap = {2: 2, 8: 1}
```

### Step 5: Check if the Number Can Be Formed

```python
for k in numberHashmap.keys():
    if numberHashmap[k] > digitHashmap[k]:
        flag = 1
```

This loop checks if the digits required to form number `i` are present in sufficient quantity in the original digits list.

* If **any digit** in `numberHashmap` exceeds its count in `digitHashmap`, we set `flag = 1` to mark it as invalid.

### Step 6: Add Valid Numbers to Result

```python
if flag == 0:
    ans.append(i)
```

If the number can be formed using the digits (i.e., `flag` is still 0), we append it to the answer list.

### Step 7: Return the Final Result

```python
return ans
```

After checking all 3-digit even numbers, return the list `ans` which contains all valid numbers that can be formed.

## Why This Works Efficiently

* We check only **even** numbers between 100 and 999 — that’s 450 numbers.
* For each number, we create a frequency map and compare it to the given digits — which is fast due to hash map usage.
* The solution avoids permutations, making it both **clean** and **efficient**, especially for the input size constraints.

## Time and Space Complexity

* **Time Complexity:** O(1), because we are only checking a fixed number of 450 possible 3-digit even numbers.
* **Space Complexity:** O(1), since the size of counters is bounded (max 10 digits).

## Final Notes

* This is a brute-force strategy done smartly.
* It avoids unnecessary permutations and handles digit counts carefully using `Counter`.
* It works well for the constraint `3 <= digits.length <= 100`.
