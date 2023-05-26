# We implement a class called Node to build our tree
class Node:
    def __init__(self, freq=0, char=None):
        self.left = None
        self.right = None
        self.char = char
        self.freq = freq
