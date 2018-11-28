class Tree():
    def __init__(self, value=None, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild


def genTree(tree):
    if tree.value >= 1:
        tree.leftChild = Tree(value=tree.value / 10)
        tree.rightChild = Tree(value=tree.value / 10)
        genTree(tree.leftChild)
        genTree(tree.rightChild)
    return tree


def printTree(tree):
    if tree:
        return [printTree(tree.leftChild)] + [tree.value] + [printTree(tree.rightChild)]
    else:
        return []


if __name__ == '__main__':
    aTree = genTree(Tree(value=100))
    print(printTree(aTree))
