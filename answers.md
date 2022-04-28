# CMPS 2200 Assignment 5
## Answers

**Name:**_________________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
If we used a greedy algorithm it would select the largest coin size first and then the next largest.
This is optimal as it converts the number to a binary number and where there is a 1 that is the coin that must be used.
In this case then the algorithm would be optimal.

- **1b.**
The runtime would be O(log(n)) to convert the integer to a binary string and then O(n) to then read that string and determine the number of coins.  This would take O(n) time overall.                   
The span would O(log(n)) for the conversion as well and since this process can be parallelized the string reading could be done in O(1) since it could be all read at once.  This would take O(log(n)) time overall.





- **2a.**
The greedy algorithm above operates on the truth that any number can be optimally represented as a sum of powers of 2, but given that this bank does not have all denominations we cannot guarantee every number can be exchanged optimally.
For example if we had denominations of (1, 6, 8) and we wanted to convert 12 dollars into coins with the greedy algorith it would be 5 coins (8, 1, 1, 1, 1) but if we used a non-greedy algorithm it would be 2 coins (6, 6) 

- **2b.**
Based on the denominations above denominations one could construct an optimal table as such:

| Dollar Amount | $1 Coin | $6 Coin | $8 Coin |
|---------------|---------|---------|---------|
| 1             | 1       | 0       | 0       |
| 2             | 2       | 0       | 0       |
| 3             | 3       | 0       | 0       |
| 4             | 4       | 0       | 0       |
| 5             | 5       | 0       | 0       |
| 6             | 0       | 1       | 0       |
| 7             | 1       | 1       | 0       |
| 8             | 0       | 0       | 1       |
| 9             | 1       | 0       | 1       |
| 10            | 2       | 0       | 1       |
| 11            | 3       | 0       | 1       |
| 12            | 0       | 2       | 0       |
| 13            | 1       | 2       | 0       |
| 14            | 0       | 1       | 1       |
| 15            | 1       | 1       | 1       |
| 16            | 0       | 0       | 2       |
| 17            | 1       | 0       | 2       |
| 18            | 0       | 3       | 0       |
| 19            | 1       | 3       | 0       |
| 20            | 2       | 3       | 0       |
| 21            | 1       | 2       | 1       |
| 22            | 0       | 1       | 2       |
| 23            | 1       | 1       | 2       |
| 24            | 0       | 0       | 3       |

With these values solved the problem would be to split a number into k amounts of each lookup.
This means that there are 16 distinct nodes to consider.  This means that there would be O(2*max-denomination) work and O(n) span because the worst case would be the bank only having $1 coins to convert.

