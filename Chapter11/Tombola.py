import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        return

    @abc.abstractmethod
    def pick(self):
        return

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))