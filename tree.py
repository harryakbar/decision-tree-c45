class node(object):
    def __init__(self, data, children = []):
        self.data = data
        if len(children) <= 0:
            self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

root = node("1")
root.add_child(node("2"))
root.add_child(node("3"))
print(root)
