## The problem
---

Description is here:

Remove all elements from a linked list of integers that have value val.

[https://leetcode.com/problems/remove-linked-list-elements/](https://leetcode.com/problems/remove-linked-list-elements/)

### Strategy
---

What we should do is just to visit all node from head skip connecting the node that has the given value. That is check each node one by one and if node.next.val is equal to a given value, connect node and node.next.next (if any).

We can use dummy head node to handle some specific case for a head node.