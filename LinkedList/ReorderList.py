"""
    143. Reorder List
    Medium

    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.


    Example 1:

    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

    Example 2:

    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]


    Constraints:

    The number of nodes in the list is in the range [1, 5 * 10^4].
    1 <= Node.val <= 1000
"""
from LinkedList.ListNode import ListNode


def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head inplace instead.
    :param head:
    :return:
    """
    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    # start from the middle and nullify it
    prev = slow.next = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # merge two halfs
    first, second = head, prev
    while second:
        # save first and second initial nodes
        temp1, temp2 = first.next, second.next
        # assign first next is second
        first.next = second
        # second next will reconnect previous saved first next
        second.next = temp1
        # keep moving forward
        first, second = temp1, temp2
        # outcome will be like "first, second, first.next, second.next"



def reorderListRecall(head: ListNode) -> None:
    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half, require current and previous node to reverse a linked list
    curr = slow.next
    prev = slow.next = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # merge two halfs with the head of initial list and reversed list head, previous node.
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        # keep moving next node
        first, second = temp1, temp2

        # # this approach works as well
        # temp1 = first.next
        # first.next = second
        # # keep moving forward to next node
        # first, second = second, temp1


def printList(node: ListNode):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

# 1,2,3,4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
printList(head)
reorderListRecall(head)
printList(head)

# 1,2,3,4,5
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
printList(node)
reorderListRecall(node)
printList(node)