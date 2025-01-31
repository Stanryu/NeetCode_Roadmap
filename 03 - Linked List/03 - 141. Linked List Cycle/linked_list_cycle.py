from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow_pointer = fast_pointer = head

        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False

if __name__ == '__main__':
    list1 = [1, 2]
    index = 0
    hub_node = next_node = linked_list = ListNode(0)
    
    while list1:
        next_node.next = ListNode(list1.pop(0))
        next_node = next_node.next
    
    if index >= 0:
        for i in range(index+1):
            hub_node = hub_node.next
        next_node.next = hub_node
    
    linked_list = linked_list.next

    s = Solution()
    print(s.hasCycle(linked_list))