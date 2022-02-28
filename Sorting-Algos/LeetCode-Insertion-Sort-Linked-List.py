# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        
        curr = head
        
        prev = curr
        curr = curr.next
        
        while curr:
            val = curr.val
            if val < prev.val:
                # remove curr from list
                prev.next = curr.next
                # first check if val is less than head.val
                if val <= head.val:
                    curr.next = head
                    head = curr
                else:
                    # loop over predecessors
                    n1 = head
                    n2 = head.next
                    while n2.val < val:
                        n1 = n1.next
                        n2 = n2.next
                    n1.next = curr
                    curr.next = n2
                # update curr and prev
                prev = prev
                curr = prev.next
            else:
                # update curr and prev
                prev = curr
                curr = curr.next
        return head


lis = list(map(int,input()[1:-1].split(",")))

# create linked list
head = ListNode(val=lis[0])
curr = head
for x in lis[1:]:
    curr.next = ListNode(val=x)
    curr = curr.next

sol = Solution()
head = sol.insertionSortList(head)

sorted_lis = []
curr = head
while curr:
    sorted_lis.append(curr.val)
    curr = curr.next
sorted_lis
