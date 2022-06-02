class Node(object):
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersRecursive(l1, l2, 0)

    def addTwoNumbersRecursive(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)
        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
        elif c:
            ret.next = Node(c)
        return ret


# 243 564 = 708
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val, end=' ')
    answer = answer.next
