class Fibonacci:
    def __iter__(self):
        return

class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a , self.b = self.b, self.a + self.b
        return result