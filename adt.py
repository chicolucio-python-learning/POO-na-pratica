"""
ADT = Abstract Data Type
"""

class IntervalMap(dict):
    def get(self, index):
        if index >= sorted(self.keys())[-1]:
            raise KeyError
        for key, value in self.items():
            if index < key:
                break
        return value