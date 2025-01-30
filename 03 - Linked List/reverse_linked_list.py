from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
       curr = head
       new_head = None
       while curr is not None:
           new_head = ListNode(curr.val, new_head)
           curr = curr.next           
       return new_head
    
if __name__ == '__main__':
    singly_linked_list = [1,2,3,4,5]
    mounted_head = None
    while(singly_linked_list):
        mounted_head = ListNode(singly_linked_list.pop(), mounted_head)
    s = Solution()
    print(s.reverseList(head = mounted_head))