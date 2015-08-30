## The problem
---

Description is here:

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

[https://leetcode.com/problems/word-break/](https://leetcode.com/problems/word-break/)

### Strategy
---

Eventually we have to use DP to solve this. The basic concept is manage a list of flags for each bit of the string. 