class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, song):
        self.queue.append(song)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
playlist = Queue()
playlist.enqueue("Song 1")
playlist.enqueue("Song 2")
playlist.enqueue("Song 3")
print("Playing:", playlist.dequeue())  # Output: Playing: Song 1
print("Playing:", playlist.dequeue())  # Output: Playing: Song 2