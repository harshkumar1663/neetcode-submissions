# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = [] 
        dummy = head
        while dummy:
            h.append(dummy)
            dummy = dummy.next
        left, right = 0, len(h)-1
        
        for i in range(len(h)-1):
            if i%2==0:
                head.next = h[right]
                right -= 1
            else:
                left += 1
                head.next = h[left]
            head = head.next
        head.next = None
 