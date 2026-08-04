# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            
            if l1 == None:
                v1 = 0
            else:
                v1 = l1.val
            
            if l2 == None:
                v2 = 0
            else:
                v2 = l2.val

            total = v1 + v2 + carry
            carry = total // 10
            new = ListNode(total % 10)
            current.next = new

            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
            
            current = current.next
        
        return dummy.next

