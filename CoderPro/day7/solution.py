class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(node)


class Solution:
    def reverse(self, node):
        if node.next is None:
            return node
        node1 = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return node1


print(Solution().reverse(node))