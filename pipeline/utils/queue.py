from queue import PriorityQueue


class UniquePriorityQueue(PriorityQueue):
    """
    Constructor for a UniquePriorityQueue, similar to the built-in PriorityQueue, but also stores elements within a Set, in order to easily
    facilitate efficiently checking for duplicates within the queue. If a duplicate object is added, then it is ignored.
    This may be changed in the future in order to change the priority of the element.
    See: https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes for more information
    """
    elements = set()

    def _put(self, item):
        if item[1] in self.elements:
            # TODO: Check if the priority of the element has changed, and if so, change the priority in the heap
            pass
        else:
            self.elements.add(item[1])
            return super(UniquePriorityQueue, self)._put(item)

    def _get(self):
        popped = super(UniquePriorityQueue, self)._get()[1]
        self.elements.remove(popped)
        return popped
