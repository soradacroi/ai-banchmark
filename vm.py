class mvm:
    def __init__(self):
        self.prev = 0
        self.curr = 1
        self.operations = {-1: self.__nop,
                           0: self.__add_one, 1: self.__sub_one,
                           2: self.__multiply, 3: self.__mod,
                           4: self.__push_to_prev,
                           5: self.__pull_to_curr,
                           6: self.__add_prev, 7: self.__rotate}
    def __add_one(self):
        self.curr += 1
    def __sub_one(self):
        self.curr -= 1
    def __multiply(self):
        self.curr *= self.prev
    def __mod(self):
        if self.prev != 0:
            self.curr = self.curr % self.prev
        else:
            self.curr = 0
    def __push_to_prev(self):
        self.prev = self.curr
        self.base_locked = True
    def __pull_to_curr(self):
        self.curr = self.prev
    def __add_prev(self):
        self.curr += self.prev
    def __rotate(self):
        self.curr, self.prev = self.prev, self.curr
    def __nop(self):
        pass
    def __output(self):
        return self.curr

    def run(self, opration_list: list) -> list[int]:
        memory: list[int] = []
        for _ in range(12):
            for i in opration_list:
                self.operations[i]()
                # -256, 256
                self.curr = ((self.curr + 128) % 257) - 128
            memory.append(self.__output())
        return memory


