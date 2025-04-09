# 🧠 Problem Understanding

You're given an array of integers `nums` and a target integer `k`. You are allowed to perform the following operation multiple times:

> Choose a valid integer `h`, and for every index `i` where `nums[i] > h`, set `nums[i] = h`.

An integer `h` is **valid** if **all** the values in the array that are strictly greater than `h` are **identical**.

Your task is to find the **minimum number of such operations** required to make **all elements in the array equal to `k`**. If it is not possible, return `-1`.

---

## ✅ Key Observations

1. If **any element is less than `k`**, it is **impossible** to reach `k` via the given operation (because we can only decrease values, never increase them).
2. For elements **greater than `k`**, we need to apply operations that step them down until they become `k`, using only valid integers `h`.
3. To avoid unnecessary operations, we should use **each unique value greater than `k` only once**, stepping down in one move.

---

## ✅ Solution Strategy

- Initialize a set `greaterthanK` to track unique values in `nums` that are greater than `k`.
- Traverse the array:
  - If any element is less than `k`, return `-1`.
  - If an element is greater than `k` and not already in the set, add it to the set and increment the operation count.
- Return the total number of operations, which is equal to the number of unique values greater than `k`.

---

## 🧪 Example Walkthrough

### Example 1:
**Input**: `nums = [5,2,5,4,5]`, `k = 2`

- Elements < 2: No ❌
- Unique values > 2: {4, 5} → Requires 2 operations
- **Output**: `2`

### Example 2:
**Input**: `nums = [2,1,2]`, `k = 2`

- Found 1 < 2 → Not allowed ❌
- **Output**: `-1`

### Example 3:
**Input**: `nums = [9,7,5,3]`, `k = 1`

- All elements > 1
- Unique values > 1: {3, 5, 7, 9} → Requires 4 operations
- **Output**: `4`

---

## ⏱️ Time & Space Complexity

- **Time Complexity**: `O(n)` where `n = len(nums)` — single pass through the array
- **Space Complexity**: `O(n)` in worst case — storing unique values in a set

---

## ✅ Summary

| Property               | Value          |
|------------------------|----------------|
| Handles invalid cases  | ✅              |
| Optimal operation count| ✅              |
| Time-efficient         | ✅ O(n)         |
| Memory usage           | ✅ O(n) set     |

