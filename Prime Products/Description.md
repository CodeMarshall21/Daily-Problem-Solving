# 📌 Problem Statement: Find a^th and b^th Prime and Compute C

## 📝 Description

You are given a string containing **two space-separated integers** `a` and `b`.

Your task is to:

1. Find the **a-th** and **b-th** prime numbers from the sequence of prime numbers.
2. Then compute the value of `C` using the formula:
   ```
   C = (a * b) - 1
   ```

> ⚠️ **Note**: Use the values of `a` and `b` directly in the formula. The prime numbers are found only for lookup purposes and are **not** used in the calculation of `C`.

---

## 📅 Input Format

- A single string containing two integers separated by a space:
  ```
  "a b"
  ```

### Constraints:
- 1 ≤ a, b ≤ 10,000

---

## 📄 Output Format

- A single integer:
  ```
  C = (a * b) - 1
  ```

---

## 🧪 Examples

### Example 1
**Input**
```
1 1
```

**Output**
```
0
```

---

### Example 2
**Input**
```
2 3
```

**Explanation**
- The 2nd prime is 3  
- The 3rd prime is 5  
- But the formula uses `a` and `b`:  
  C = (2 * 3) - 1 = **5**

**Output**
```
5
```

---

### Example 3
**Input**
```
4 6
```

**Output**
```
23
```

