# Approach 4: Hash Set

## Algorithm
- Create a hash set unpaired to track numbers that havent found their pairs yet.
- For each number num in nms .
    - If run is already in unpaired remove it (we found its pair).
    - Else, add it to unpaired (waiting for its pair).
- Check if unpaired is empty:
    - If empty, return true as all numbers found their pairs.
    - If not empty, return false .