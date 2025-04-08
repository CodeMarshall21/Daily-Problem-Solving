# 📘 Description

## 🔍 Problem Description

You are given an array of integers `nums`. Your task is to make all the elements in the array **distinct** by performing the following operation any number of times:

> ✅ **Operation**: Remove the **first 3 elements** from the array.  
> If the array has fewer than 3 elements, remove **all** remaining elements.

An **empty array** is considered to contain only **distinct** elements.

Return the **minimum number of operations** required to make all the elements in the array distinct.

---

## 💡 Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

---

## 🧪 Examples

### Example 1:

**Input**:  
`nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]`  

**Output**:  
`2`

**Explanation**:  
- After 1st operation → `[4, 2, 3, 3, 5, 7]`  
- After 2nd operation → `[3, 5, 7]` → all elements are distinct

---

### Example 2:

**Input**:  
`nums = [4, 5, 6, 4, 4]`  

**Output**:  
`2`

**Explanation**:  
- After 1st operation → `[4, 4]`  
- After 2nd operation → `[]` → empty array is considered distinct

---

### Example 3:

**Input**:  
`nums = [6, 7, 8, 9]`  

**Output**:  
`0`

**Explanation**:  
All elements are already distinct.

---
