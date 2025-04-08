
# 🧠 Problem Statement

You are given an integer array `nums`. You need to ensure that all elements in the array are **distinct**. To achieve this, you can perform the following operation **any number of times**:

> **Operation**: Remove **3 elements from the beginning** of the array. If the array has fewer than 3 elements, remove **all** remaining elements.

An **empty array** is considered to have **distinct** elements.

---

## ✅ Objective

Return the **minimum number of operations** required to make all the elements in the array distinct.

---

## 🧮 Code Implementation

```python
class Solution:
    def minimumOperations(self, nums):
        times = 0
        while len(nums) != len(set(nums)):
            times += 1
            nums = nums[3:]
        return times
```

---

## 🔍 Explanation of the Code

### 🔁 Loop Until All Elements Are Distinct

The condition:
```python
while len(nums) != len(set(nums)):
```
keeps checking if the array still has **duplicate elements**. If the length of `nums` is not equal to the number of **unique elements** (`set(nums)`), it means there are duplicates.

### 🧹 Removing Elements

Every time duplicates are found:
```python
nums = nums[3:]
```
removes the **first 3 elements** from the array.

If fewer than 3 elements are left, Python safely slices them off, leaving the array empty.

### 🔢 Counting the Operations

The variable:
```python
times += 1
```
counts how many such removal operations are performed.

Once the array becomes distinct (or empty), the loop stops, and `times` is returned.

---

## 💡 Example Walkthrough

### Example 1:
**Input**: `[1,2,3,4,2,3,3,5,7]`

- After 1st operation → `[4,2,3,3,5,7]` (Still duplicates)
- After 2nd operation → `[3,5,7]` (All unique)

**Output**: `2`

---

### Example 2:
**Input**: `[4,5,6,4,4]`

- After 1st operation → `[4,4]` (Still duplicates)
- After 2nd operation → `[]` (Empty array is distinct)

**Output**: `2`

---

### Example 3:
**Input**: `[6,7,8,9]`

- Already all elements are distinct.

**Output**: `0`

---

## ✅ Time Complexity

- **Worst Case**: O(N²)  
  Due to slicing and converting to a set in every iteration.

- **Best Case**: O(1)  
  If the array is already distinct.

---

## 📌 Constraints Handled

- The code handles small arrays (less than 3 elements) gracefully due to safe slicing.
- Ensures that the loop ends once the array is either empty or all elements are distinct.

---
