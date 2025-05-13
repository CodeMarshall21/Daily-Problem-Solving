# Problem: 2094 - Finding 3-Digit Even Numbers

## Description

You are given an array of digits, where each digit is an integer between 0 and 9. Your task is to find all unique three-digit **even** numbers that can be formed by concatenating **three distinct elements** from the array in any order.

Each resulting number must meet the following criteria:

1. It must be a 3-digit number (no leading zeros).
2. It must be an even number (i.e., the last digit is 0, 2, 4, 6, or 8).
3. You can only use each digit as many times as it appears in the input array.
4. The resulting list of numbers must be sorted in **increasing order** and contain only **unique** values.

## Examples

### Example 1:

**Input:**

```
digits = [2, 1, 3, 0]
```

**Output:**

```
[102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
```

**Explanation:**
All valid combinations that satisfy the rules are returned in sorted order.

### Example 2:

**Input:**

```
digits = [2, 2, 8, 8, 2]
```

**Output:**

```
[222, 228, 282, 288, 822, 828, 882]
```

**Explanation:**
Duplicate digits are used as often as they appear.

### Example 3:

**Input:**

```
digits = [3, 7, 5]
```

**Output:**

```
[]
```

**Explanation:**
No valid 3-digit even number can be formed.

## Constraints

* `3 <= digits.length <= 100`
* `0 <= digits[i] <= 9`

