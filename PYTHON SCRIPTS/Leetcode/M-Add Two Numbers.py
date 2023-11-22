# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.convert(l1)
        num2 = self.convert(l2)
        num3 = num1 + num2
        return self.convert_to_list(num3)

    def convert(self, node):
        list1 = []
        while node:
            list1.append(str(node.val))
            node = node.next
        list1.reverse()
        return int(''.join(list1))
    
    def convert_to_list(self, l3):
        list2 = []
        if not l3:
            list2.append(l3)
        while l3:
            list2.append(l3 % 10)
            l3 //= 10
        dummy = ListNode()
        curr = dummy
        for digit in list2:
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next
'''    
this code returns the reverse of the sum of two linked lists
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''