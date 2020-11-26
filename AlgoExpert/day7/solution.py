import heapq


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.max, x)

    def pop(self) -> None:
        ele = self.stack.pop()
        self.max.remove(ele)
        heapq.heapify(self.max)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.max[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()