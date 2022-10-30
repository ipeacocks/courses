class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # construct a dummy node
        dummy = ListNode(0)
        dummy.next = head 

        # set up pre and cur pointers
        pre = dummy
        cur = head
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # propose the next for pre
                # this will be verified by next line
                cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next