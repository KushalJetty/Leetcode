# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next

        tail.next = list1 or list2

        return dummy.next
    def mergeTwoLists(self, list1, list2):
        if not list1: return list2
        if not list2: return list1

        if list1.val < list2.val:
            head = tail = list1
            list1 = list1.next
        else:
            head = tail = list2
            list2 = list2.next

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return head

            
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next, node2.next = node2, node3
node4.next, node5.next = node5, node6

obj = Solution()
obj.mergeTwoLists(node1,node4)
