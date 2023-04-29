class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self, n):
        if self is None:
            return
        if self.right:
            self.right.PrintTree(n + 1)
        print('\t' * n, self.data)
        if self.left:
            self.left.PrintTree(n + 1)

    def __add__(self, node):
        if node < self.data:
            if self.left is None:
                self.left = Tree(node)
            else:
                self.left.__add__(node)
        elif node > self.data:
            if self.right is None:
                self.right = Tree(node)
            else:
                self.right.__add__(node)


t = Tree(10)
t.__add__(7)
t.__add__(4)
t.__add__(8)
t.__add__(12)
t.__add__(15)
t.__add__(14)
t.PrintTree(0)