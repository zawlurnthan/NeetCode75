"""
    206. Reverse Linked List
    Easy

    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:

    Input: head = [1,2]
    Output: [2,1]

    Example 3:

    Input: head = []
    Output: []


    Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000


    Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from LinkedList.ListNode import ListNode


def reverseList(head: ListNode) -> ListNode:
    prev, curr = None, head

    # prev, curr, next
    # curr, next, prev
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverseListMine(head: ListNode) -> ListNode:
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def reverseListSomeoneElse(head: ListNode) -> ListNode:
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def printList(node: ListNode):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
printList(head)
# printList(reverseList(head))
# printList(reverseListMine(head))
printList(reverseListSomeoneElse(head))