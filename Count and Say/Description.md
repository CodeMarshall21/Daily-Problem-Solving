# 38. Count and Say

**Difficulty:** Medium

---

## Problem Statement

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- `countAndSay(1)` = "1"
- `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the **count of characters followed by the character itself**.

For example:
- To compress the string "3322251" using RLE:
  - Replace "33" with "23"
  - Replace "222" with "32"
  - Replace "5" with "15"
  - Replace "1" with "11"
  - Final result: "23321511"

### Input:
A positive integer `n` (1 <= n <= 30).

### Output:
Return the `n`th term in the count-and-say sequence as a string.

---

## Examples

### Example 1:
**Input:**
```
n = 4
```
**Output:**
```
"1211"
```
**Explanation:**
```
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
```

### Example 2:
**Input:**
```
n = 1
```
**Output:**
```
"1"
```
**Explanation:**
```
This is the base case.
```

---

## Constraints
- 1 <= n <= 30

---

## Follow-up:
Can you solve this problem **iteratively**?

---

## Tags:
- String
- Recursion

---

