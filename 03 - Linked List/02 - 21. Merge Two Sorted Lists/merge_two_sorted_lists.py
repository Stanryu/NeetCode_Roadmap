from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(list: list) -> Optional[ListNode]:
    singly_linked_list_head = None
    while list:
        singly_linked_list_head = ListNode(list.pop(), singly_linked_list_head)
    return singly_linked_list_head

def print_node(head: Optional[ListNode]):
    if head is None:
        print("Vazio")
    text = str(head.val)
    while head.next:
        text = text + ', ' + str(head.next.val)
        head = head.next
    print(text)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_head = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
                
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return new_head.next


if __name__ == '__main__':
    a = [0,1,2,4,7,9]
    b = [3,5,8,12]

    list1 =  list_to_linked_list(a)
    list2  = list_to_linked_list(b)

    print_node(list1)
    print_node(list2)

    s = Solution()
    print_node(s.mergeTwoLists(list1, list2))