"""
    21. Merge Two Sorted Lists
    Easy

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing
    together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:

    Input: list1 = [], list2 = []
    Output: []

    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]


    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
from LinkedList.ListNode import ListNode


def mergeTowLists(l1: ListNode, l2: ListNode) -> ListNode:
    prev = ListNode()
    node = prev

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    if l1:
        node.next = l1
    else:
        node.next = l2

    return prev.next


def printList(node: ListNode):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)

node = ListNode(1)
node.next = ListNode(3)
node.next.next = ListNode(4)
printList(mergeTowLists(head, node))