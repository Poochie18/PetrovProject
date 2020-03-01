class LCM:
    def __init__(self):
        pass
    def lcm(self,b):
        self = abs(self)
        b = abs(b)
        i = min(self, b)
        while True:
            if i % self == 0 and i % b == 0:
                break
            i += 1
        return i