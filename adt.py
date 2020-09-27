"""
ADT = Abstract Data Type
"""


class IntervalMap:
    def __init__(self):
        self.limits = []
        self.map = {}

    def __setitem__(self, upper_bound, value):
        self.limits.append(upper_bound)
        self.limits.sort()
        self.map[upper_bound] = value

    def get(self, index):
        if index >= self.limits[-1]:
            raise KeyError
        for upper_bound in self.limits:
            if index < upper_bound:
                break
        return self.map[upper_bound]
