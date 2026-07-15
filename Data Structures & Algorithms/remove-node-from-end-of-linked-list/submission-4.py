# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        cur=dummy
        ind=head
        k=1
        while ind.next:
            k+=1
            ind=ind.next

        for _ in range(k-n):
            cur=cur.next
        cur.next=cur.next.next
        return dummy.next