# 1805. Number of Different Integers in a String

## Solution:

Use 2 points one for start (`startIndex`) and one for end (`i`). Walk through each character in word, 
- If not digit, update start point,
- If leading zero, update start point,
- Otherwise, go next one.


## Heads up

- The number can be overflow if using `int`
- Don't forget the last one (Either add to set after loop, or add dummy end character to original word)