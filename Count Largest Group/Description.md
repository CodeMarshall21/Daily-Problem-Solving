# 1399. Count Largest Group

**Difficulty:** Easy

---

## Problem Statement
You are given an integer `n`.

Each number from `1` to `n` is grouped according to the **sum of its digits**.

Return the **number of groups** that have the **largest size**.

---

## Example 1:
**Input:**
```
n = 13
```
**Output:**
```
4
```
**Explanation:**
There are 9 groups based on the sum of digits:
- Sum 1: [1,10]  
- Sum 2: [2,11]  
- Sum 3: [3,12]  
- Sum 4: [4,13]  
- Sum 5: [5]  
- Sum 6: [6]  
- Sum 7: [7]  
- Sum 8: [8]  
- Sum 9: [9]  

The groups [1,10], [2,11], [3,12], and [4,13] all have size 2, which is the largest. So, the result is **4**.

---

## Example 2:
**Input:**
```
n = 2
```
**Output:**
```
2
```
**Explanation:**
- Sum 1: [1]  
- Sum 2: [2]  

There are 2 groups with size 1 (the largest), so the result is **2**.

---

## Constraints:
- `1 <= n <= 10^4`

---


## Related Topics:
- Hash Table
- Counting

