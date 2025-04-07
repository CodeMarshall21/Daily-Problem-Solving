# 🔍 Code Explanation: `primeFinder(nums)`

## 📄 Function Overview
The `primeFinder(nums)` function takes a list of two integers `nums`, finds the **a-th** and **b-th** prime numbers, and returns:
```
(prime_a * prime_b) - 1
```

Where:
- `prime_a` is the a-th prime number
- `prime_b` is the b-th prime number

---

## ✅ Step-by-Step Explanation

### 1. **Initialization**
```python
primes = [True] * (max(nums)**2)
```
- We create a boolean list `primes` large enough to ensure it contains at least the a-th and b-th primes.
- `max(nums)**2` is used as an upper bound to safely cover the required number of primes.

```python
primes[0] = primes[1] = False
```
- Set 0 and 1 to `False` as they are not prime numbers.

---

### 2. **Sieve of Eratosthenes**
```python
while(i*i < primesLen):
    if (primes[i]):
        for j in range(i*i, primesLen, i):
            primes[j] = False
    i += 1
```
- Classic Sieve of Eratosthenes algorithm to mark all non-prime numbers as `False`.
- Optimization: Only loop while `i*i <= primesLen` because if a number has a factor greater than its square root, the smaller corresponding factor would have already marked it.

---

### 3. **Collect Prime Numbers**
```python
for num in range(primesLen):
    if (primes[num]):
        primeNums.append(num)
```
- Collect all numbers marked as `True` (i.e., primes) into the `primeNums` list.

---

### 4. **Prime Lookup and Final Calculation**
```python
return (primeNums[nums[0]-1] * primeNums[nums[1]-1]) - 1
```
- Retrieve the a-th and b-th prime numbers by their index (`nums[0]-1` and `nums[1]-1`) since indexing starts at 0.
- Return the product of those two primes minus 1.

---

## 📅 Input Handling
```python
val = input().split()
nums = []
for i in val:
    if i != " ":
        nums.append(int(i))
```
- Takes a string of space-separated integers from the user.
- Converts them to integers and stores them in `nums`.

---

## 📊 Example
**Input:**
```
2 3
```
**Processing:**
- 2nd prime = 3
- 3rd prime = 5
- Calculation: (3 * 5) - 1 = **14**

**Output:**
```
14
```

---

## 👉 Summary
This function efficiently uses the **Sieve of Eratosthenes** to find required prime numbers and performs a basic arithmetic operation to compute the final answer. The approach ensures scalability for large values of `a` and `b` up to 10,000.