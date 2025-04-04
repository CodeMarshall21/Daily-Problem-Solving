### ✅ Explanation
---
Video -> [Maximum Value of an Ordered Triplet II - Leetcode 2874 - Python](https://www.youtube.com/watch?v=yWlxzvpU6WY)
---
#### Efficient Approach Explained

To solve this problem efficiently in **O(n)** time, we avoid checking all `O(n³)` or `O(n²)` triplets and instead use a **greedy + prefix tracking strategy**.

---

### 🔧 Core Idea:

We want to compute:

```
(nums[i] - nums[j]) * nums[k]
```

with `i < j < k`.

Rewriting this expression:
```
= (prefix_max_before_j - nums[j]) * nums[k]
```

So, the idea is:
- As we move forward, we maintain the **maximum value encountered so far** (`prefixMax`) for `nums[i]`.
- For each position `j`, we compute the best `prefixMax - nums[j]`, and store the maximum of that in `maxDiff`.
- For each `k`, the value becomes: `maxDiff * nums[k]`.

---

### 🧠 Step-by-step:

1. **prefixMax**: Track the largest number we've seen so far (potential `nums[i]`).
2. **maxDiff**: Track the maximum value of `nums[i] - nums[j]` seen so far (to multiply with `nums[k]`).
3. **res**: At each index `k`, update the result as `max(res, maxDiff * nums[k])`.

---

### ✅ Code Logic

```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefixMax = nums[0]
        maxDiff = 0
        res = 0
        
        for k in range(1, len(nums)):
            res = max(res, maxDiff * nums[k])            # Use max diff till now with current nums[k]
            maxDiff = max(maxDiff, prefixMax - nums[k])  # Update max difference so far
            prefixMax = max(prefixMax, nums[k])          # Update prefix max for future iterations
            
        return res
```

---

### 🧪 Time & Space Complexity:

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` — only a few variables used

---


---

### 🔍 Dry-Run + Visual Understanding

Let’s walk through **Example: `nums = [12, 6, 1, 2, 7]`** step-by-step using your approach.

#### Initialize:
- `prefixMax = 12` (nums[0])
- `maxDiff = 0`
- `res = 0`

---

### 🔄 Iteration-wise updates:

#### 🔹 Step k = 1 → nums[1] = 6
- `maxDiff = max(0, 12 - 6) = 6`
- `res = max(0, 6 * 6) = 36`
- `prefixMax = max(12, 6) = 12`

#### 🔹 Step k = 2 → nums[2] = 1
- `maxDiff = max(6, 12 - 1) = 11`
- `res = max(36, 11 * 1) = 36`
- `prefixMax = max(12, 1) = 12`

#### 🔹 Step k = 3 → nums[3] = 2
- `maxDiff = max(11, 12 - 2) = 11`
- `res = max(36, 11 * 2) = 36`
- `prefixMax = max(12, 2) = 12`

#### 🔹 Step k = 4 → nums[4] = 7
- `maxDiff = max(11, 12 - 7) = 11`
- `res = max(36, 11 * 7) = 77` ✅

---

### 📊 Final Output: `77`

Which matches the best triplet: `(0, 2, 4)` → `(12 - 1) * 7 = 77`

---

### 🎯 Visual Snapshot

| k | nums[k] | prefixMax | maxDiff (max(nums[i] - nums[j])) | Current Triplet Value | res |
|---|---------|-----------|-----------------------------------|------------------------|-----|
| 1 |    6    |    12     |           6                      |     6 × 6 = 36         | 36  |
| 2 |    1    |    12     |           11                     |     11 × 1 = 11        | 36  |
| 3 |    2    |    12     |           11                     |     11 × 2 = 22        | 36  |
| 4 |    7    |    12     |           11                     |     11 × 7 = 77        | 77 ✅|

---

Would you like a diagram to represent the i–j–k selection visually too (maybe with arrows on the array)?
