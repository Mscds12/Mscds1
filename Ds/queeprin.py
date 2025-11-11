class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, document):
        self.queue.append(document)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
printer = Queue()
printer.enqueue("Document 1")
printer.enqueue("Document 2")
printer.enqueue("Document 3")
print("Printing:", printer.dequeue())  # Output: Printing: Document 1
print("Printing:", printer.dequeue())  # Output: Printing: Document 2
print("Printing:", printer.dequeue())  # Output: Printing: Document 3
if printer.is_empty():
    print("Printer is idle")  # Output: Printer is idle