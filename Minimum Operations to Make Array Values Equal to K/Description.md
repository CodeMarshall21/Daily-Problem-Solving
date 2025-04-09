# 📘 description.md

## 🧾 Problem Statement

You are given an integer array `nums` and an integer `k`.

An integer `h` is called **valid** if all values in the array that are **strictly greater** than `h` are **identical**.

For example, if `nums = [10, 8, 10, 8]`, a valid integer is `h = 9` because all `nums[i] > 9` are equal to `10`. However, `h = 5` is not a valid integer because the elements greater than 5 are not all the same (they include both 8 and 10).

You are allowed to perform the following operation on `nums`:

- Select an integer `h` that is **valid** for the current array.
- For each index `i` where `nums[i] > h`, set `nums[i] = h`.

Your task is to return the **minimum number of operations** required to make **every element in `nums` equal to `k`**. If it is impossible to make all elements equal to `k`, return `-1`.

---

## 🔒 Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`

---

## 🧪 Examples

### Example 1
**Input**: `nums = [5,2,5,4,5]`, `k = 2`  
**Output**: `2`

### Example 2
**Input**: `nums = [2,1,2]`, `k = 2`  
**Output**: `-1`

### Example 3
**Input**: `nums = [9,7,5,3]`, `k = 1`  
**Output**: `4`

