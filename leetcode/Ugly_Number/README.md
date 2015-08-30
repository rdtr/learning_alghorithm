## The problem
---

Description is here:

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

[https://leetcode.com/problems/ugly-number/](https://leetcode.com/problems/ugly-number/)

### Strategy
---

Continue to divide by 2, 3, and 5 until it becomes not dividible.
After that, if the number is ugly, the result should be 1. Then if not, return True.