# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        try:
            current = l1
            a1 = [current.val]
            while current.next:
                current = current.next
                a1.append(current.val)
        except:
            a1 = []
        
        try:
            current = l2
            a2 = [current.val]
            while current.next:
                current = current.next
                a2.append(current.val)
        except:
            a2 = []
        
        a3 = a1 + a2
        a3.sort()
        if a3 == []:
            return ListNode("")
        
        l3 = ListNode(a3[0])
        current = l3
        
        for new_element in a3[1:]:
            current.next = ListNode()
            current = current.next
            current.val = new_element
        return l3


# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
#         dummy = temp = ListNode(0)
#         while l1 != None and l2 != None:

#             if l1.val < l2.val:
#                 temp.next = l1
#                 l1 = l1.next
#             else: 
#                 temp.next = l2
#                 l2 = l2.next
#             temp = temp.next
#         temp.next = l1 or l2
#         return dummy.next