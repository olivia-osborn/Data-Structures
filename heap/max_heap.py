class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        self.storage[0], self.storage[len(
            self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
        removed = self.storage.pop()
        self._sift_down(0)
        return removed

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # loop until either the element reaches the top of the array
        # or we'll break the loop when we realize the element's priority
        # is not larger than it's parent's value
        while index > 0:
            # the value at index fetches index of parent
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # update index:
                index = parent
            else:
                # otherwise element has reached spot where it belongs
                break

    def _sift_down(self, index):
        # loop until either the element reaches the end of the array
        # or we'll break the loop
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        largest = index
        if left_child in range(len(self.storage)-1) and self.storage[left_child] > self.storage[largest]:
            largest = left_child
        if right_child in range(len(self.storage)-1) and self.storage[right_child] > self.storage[largest]:
            largest = right_child
        if self.storage[largest] > self.storage[index]:
            self.storage[largest], self.storage[index] = self.storage[index], self.storage[largest]
            self._sift_down(largest)

    def __str__(self):
        return f'arr: {self.storage}'


hp = Heap()
hp.insert(5)
hp.insert(9)
hp.insert(15)
hp.insert(4)
hp.insert(45)
hp.insert(22)

hp.delete()

# hp.insert(6)
# hp.insert(8)
# hp.insert(10)
# hp.insert(9)
# hp.insert(1)
# hp.insert(9)
# hp.insert(9)
# hp.insert(5)
# hp.delete()

print(hp)
