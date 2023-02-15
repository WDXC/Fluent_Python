from random import randrange

from Tombola import Tombola

@Tombola.register
class TomboList(list):
    def pick(self):
       if self:
           position = randrange(len(self))
           return self.pop(position)
       else:
           raise LookupError('pop from empty TomboList')

    load = list.extend()

    def loaded(self):
        return bool(self)

    def inspct(self):
        return tuple(sorted(self))