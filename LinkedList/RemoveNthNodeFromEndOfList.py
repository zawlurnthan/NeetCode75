"""
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""
from LinkedList.ListNode import ListNode


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # a node to return
    dummy = ListNode(0, head)
    left, right = dummy, head

    # fast moves n node ahead
    while n > 0:
        right = right.next
        n -= 1

    # move right pointer till the end of the list
    # slow surprisingly iterate three time while fast does twice
    while right:
        left = left.next
        right = right.next

    # delete nth node
    left.next = left.next.next
    return dummy.next


def removeNthFromEndSomeoneElseWay(head: ListNode, n: int) -> ListNode:
    """
        solve problem with two pointers. Fast pointer moves n nodes ahead of Slow pointer,
        move together then. While Fast pointer is at the end of the list, Slow pointer
        reaches nth node from the end. by skipping nth node of the Slow pointer, problem
        is solved.

    :param head:
    :param n:
    :return:
    """
    slow, fast = head, head

    # fast moves n node ahead of slow
    for i in range(n): fast = fast.next
    if not fast: return head.next

    # move until end of the list
    # next is required to stop the slow from iterating one more loop
    while fast.next:
        fast, slow = fast.next, slow.next

    # skip/delete nth node
    slow.next = slow.next.next
    return head


def printList(node: ListNode):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


# 1,2,3,4,5
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
printList(node)
# printList(removeNthFromEnd(node, 2))
printList(removeNthFromEndSomeoneElseWay(node, 2))



