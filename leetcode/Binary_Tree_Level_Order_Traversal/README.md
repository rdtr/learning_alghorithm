## The problem
---

Description is here:

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

[https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/)

### Strategy
---

If we can just output a path of BFS, it's possible to just use a single queue to manage the order of traversal. But in this question, we have to store an each level of node too.

One simple way is use two queues to manage parents and their children.
One queue stores parents of the same level and another stores children of them and after all treversal of children is done, move them into parents' queue because they become parents at next step.