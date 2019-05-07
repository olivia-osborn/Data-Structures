"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        # if list is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = new_node
        self.length += 1

    def remove_from_head(self):
        # if list is empty:
        if not self.head and not self.tail:
            return None
        # if one item in list:
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return self.head
        else:
            old_head = self.head
            self.delete(self.head)
            return old_head.value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        # if list is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        deleted_node = ListNode(node)
        deleted_node.delete()

    def get_max(self):
        pass

    def __str__(self):
        return f'head: {self.head.value}, tail: {self.tail.value}, length: {self.length}'


dll = DoublyLinkedList()
dll.add_to_head(5)
dll.add_to_head(2)
dll.add_to_head(1)
dll.add_to_tail(9)
dll.delete(9)

print(dll)
