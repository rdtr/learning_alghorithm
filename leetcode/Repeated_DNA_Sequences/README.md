## The problem
---

Description is here:

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

[https://leetcode.com/problems/repeated-dna-sequences/](https://leetcode.com/problems/repeated-dna-sequences/)

### Strategy
---

We don't need to use some specific algorithm like KMP or BM.
Just retrieving all possible 10 characters from a head of the given string and check its apperance count by dictionary suffices.