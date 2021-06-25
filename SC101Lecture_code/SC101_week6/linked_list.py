"""
File: linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


class ListNode:
	def __init__(self, data, pointer):
		# value & next 為慣用語
		self.value = data
		self.next = pointer


def main():
	# Way 1
	node1 = ListNode(('A', 3), None)
	node2 = ListNode(('B', 5), None)
	node1.next = node2
	node3 = ListNode(('C', 7), None)
	node2.next = node3

	# Way 2
	node3 = ListNode(('C', 7), None)
	node2 = ListNode(('B', 5), node3)
	node1 = ListNode(('A', 3), node2)
	linked_list = node1
	traversal(linked_list)


def traversal(linked_list):
	cur = linked_list
	while cur is not None:
		print(cur.value)
		cur = cur.next


if __name__ == '__main__':
	main()
