class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li=[]
        if not head: return
        while head:
            li.append(head.val)
            head = head.next
        dummy = ListNode()
        curr = dummy 
        if k>len(li): k=k%len(li)
        for i in li[len(li)-k:]:
            curr.next = ListNode(i)
            curr = curr.next
        for i in li[:len(li)-k]:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
    
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]