"""
File: priority_queue_linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It controls the condition to break the input loop
EXIT = ''


class ListNode:
	def __init__(self, val, next_one):
		self.val = val
		self.next = next_one


def main():
	priority_queue = None
	while True:
		name = input(f'Name of patient ({EXIT} to quit): ')
		if name == EXIT:
			break
		priority = int(input('Priority: '))
		data = (name, priority)
		if priority_queue is None:
			priority_queue = ListNode(data, None)
		else:
			if priority_queue.val[1] > priority:
				# New node at the beginning
				new_node = ListNode(data, None)
				new_node.next = priority_queue
				priority_queue = new_node
			else:
				cur = priority_queue
				# New node in between
				while cur.next is not None:
					if cur.val[1] <= priority < cur.next.val[1]:
						new_node = ListNode(data, None)
						new_node.next = cur.next
						cur.next = new_node
						break
					cur = cur.next
				# New node at the end
				if cur.next is None:
					new_node = ListNode(data, None)
					cur.next = new_node
	traversal(priority_queue)


def traversal(linked_list):
	cur = linked_list
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
