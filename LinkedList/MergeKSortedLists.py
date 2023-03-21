"""
    23. Merge k Sorted Lists
    Hard

    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.


    Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

    Example 2:

    Input: lists = []
    Output: []

    Example 3:

    Input: lists = [[]]
    Output: []


    Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10^4.
"""
import heapq
from queue import PriorityQueue
from typing import List
from LinkedList.ListNode import ListNode


def mergeKLists(lists: List[ListNode]) -> ListNode:
    if not lists or len(lists) == 0: return None

    while len(lists) > 1:
        mergedLists = []
        # merge two lists each time
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # check if l2 is within lists
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        # stop the while loop
        lists = mergedLists
    return lists[0]


def mergeList(l1, l2):
    dummy = ListNode()
    node = dummy

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
    return dummy.next


def mergeKListsWithPQ(lists: List[ListNode]) -> ListNode:
    head = tail = ListNode(None)
    pq = PriorityQueue()

    def addNodeInPQ(index, node):
        if node:
            pq.put((node.val, index, node))

    for index, node in enumerate(lists):
        addNodeInPQ(index, node)

    while not pq.empty():
        _, index, node = pq.get()
        addNodeInPQ(index, node.next)
        node.next = None
        tail.next = node
        tail = tail.next
    return head.next


def mergeKListsWithHeap(lists: List[ListNode]) -> ListNode:
    h = []
    head = tail = ListNode(0)

    for i in range(len(lists)):

        # heapq.heappush(heap, item)
        heapq.heappush(h, (lists[i].val, i, lists[i]))
        print(lists[i].val)
    print()

    while h:
        node = heapq.heappop(h)
        print(node[0], node[1], node[2].val)
        node = node[2]
        tail.next = node
        tail = tail.next
        if node.next:
            i += 1
            heapq.heappush(h, (node.next.val, i, node.next))
            print(node.next.val)
    return head.next


def printList(node: ListNode):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(5)

node = ListNode(1)
node.next = ListNode(3)
node.next.next = ListNode(4)

lead = ListNode(2)
lead.next = ListNode(6)

lists = [head, node, lead]
# printList(mergeKLists(lists))
# printList(mergeKListsWithPQ(lists))
printList(mergeKListsWithHeap(lists))
