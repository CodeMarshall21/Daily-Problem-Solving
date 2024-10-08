# Longest Consecutive Sequence
1. we create a set of nums array to remove duplicates `numSet`
2. for every number in nums array, we check wether it is the starting of sequence `if (num-1) not in nums_set`
3. if yes, we increment the number of elements of that sequence `count`
4. we check for all elements of that particular sequence untill we reach the end of sequence `while (num + count) in nums_set`
5. once we reach the end of sequence, we update it with max_count {if only current "count" is greater} `max_count = max(count, max_count)`
6. now return `max_count`
