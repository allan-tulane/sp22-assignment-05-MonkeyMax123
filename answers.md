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

| Dollar Amount | $1 Coin | $6 Coin | $8 Coin | minimum |
|---------------|---------|---------|---------|---------|
| 1             | 1       | 0       | 0       | 1       |
| 2             | 2       | 0       | 0       | 2       |
| 3             | 3       | 0       | 0       | 3       |
| 4             | 4       | 0       | 0       | 4       |
| 5             | 5       | 0       | 0       | 5       |
| 6             | 6       | 1       | 0       | 1       |
| 7             | 7       | 2       | 0       | 2       |
| 8             | 8       | 3       | 1       | 1       |
| 10            | 10      | 5       | 3       | 3       |
| 11            | 11      | 6       | 4       | 4       |
| 12            | 12      | 2       | 5       | 2       |
| 13            | 13      | 3       | 6       | 3       |
| 14            | 14      | 4       | 2       | 2       |
| 15            | 15      | 5       | 3       | 3       |
| 16            | 16      | 6       | 2       | 2       |
| 17            | 17      | 7       | 3       | 3       |
| 18            | 18      | 3       | 4       | 3       |
| 19            | 19      | 4       | 5       | 4       |
| 20            | 20      | 5       | 3       | 3       |
| 21            | 21      | 6       | 4       | 4       |
| 22            | 22      | 7       | 5       | 5       |
| 23            | 23      | 8       | 6       | 6       |
| 24            | 24      | 4       | 3       | 3       |

if Dk(largest denomination)
(n-Dk, k) + 1

if Dk cannot be used
(n, k-1)

min((n-Dk, k) + 1, (n, k[1:]))

Given that n = the amount of money and k = the number of possible denomination
The DAG would have n*k nodes meaning that the work would be O(n*k) with a span of O(n).

