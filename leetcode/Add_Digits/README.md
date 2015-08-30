## The problem
---

Description is here:

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

[https://leetcode.com/problems/add-digits/](https://leetcode.com/problems/add-digits/)

### Strategy
---

We can do it by recursively calculating the sum while the digit becomes 1.
Or we can use the formula written in here: https://en.wikipedia.org/wiki/Digital_root