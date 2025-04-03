# Problem Description

## Title: Consecutive Vowel and Consonant Replacement

### Problem Statement:

Write a function that takes a string as input and replaces consecutive vowels with 'V' and consecutive consonants with 'C'. The function should iterate through the string and categorize each segment of consecutive vowels or consonants appropriately.

### Input:

- A lowercase string consisting of English alphabet letters (`a-z`).
- The input string will have at least one character.

### Output:

- A transformed string where:
  - Consecutive vowels (`a, e, i, o, u`) are replaced with a single 'V'.
  - Consecutive consonants (`b, c, d, ..., z` except vowels) are replaced with a single 'C'.

### Constraints:

- The input string will contain only lowercase English letters (`a-z`).
- Length of the input string: `1 <= len(s) <= 1000`.

### Example Cases:

#### Example 1:

**Input:**

```
youhurt
```

**Output:**

```
CVCVC
```

#### Example 2:

**Input:**

```
aaiiouu
```

**Output:**

```
V
```

#### Example 3:

**Input:**

```
bcdfg
```

**Output:**

```
C
```

#### Example 4:

**Input:**

```
queue
```

**Output:**

```
CV
```

### Notes:

- The function must correctly identify consecutive sequences and replace them with a single 'V' or 'C'.
- Single vowels or consonants should still be replaced with 'V' or 'C' respectively.

