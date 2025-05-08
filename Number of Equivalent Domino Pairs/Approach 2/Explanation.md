## Approach: Tuple Representation + Counting
---
Intuition
In this problem, we need to count all equivalent dominoes, where dominoes are represented by pairs. The definition of "equivalent" is that, under the condition of allowing the flip of two pairs, their elements correspond and are equal one by one.

So we might as well directly convert each binary pair into the specified format, that is, the first dimension must not be greater than the second dimension. Two pairs are equivalent if they contain the same two numbers, regardless of order.

Noticing that the elements in the pairs are all not greater than 9, we can concatenate each binary pair into a two-digit positive integer, i.e., (x,y)→10x+y. In this way, there is no need to use a hash table to count the number of elements, but we can directly use an array of length 100.


[Python Tutor Explanation](https://pythontutor.com/visualize.html#code=def%20numEquivDominoPairs%28dominoes%29%3A%0A%20%20%20%20%20%20%20%20num%20%3D%20%5B0%5D%20*%20100%0A%20%20%20%20%20%20%20%20pairs%20%3D%200%0A%20%20%20%20%20%20%20%20for%20x,%20y%20in%20dominoes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20x%20*%2010%20%2B%20y%20if%20x%20%3C%3D%20y%20else%20y%20*%2010%20%2B%20x%0A%20%20%20%20%20%20%20%20%20%20%20%20pairs%20%2B%3D%20num%5Bval%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20num%5Bval%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%20ret%0A%0Adominoes%20%3D%20%5B%5B1,2%5D,%5B1,2%5D,%5B1,1%5D,%5B1,2%5D,%5B2,2%5D%5D%0A%0Aprint%28numEquivDominoPairs%28dominoes%29%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)