class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


class BinaryTree:
    def __init__(self, root_node):
        self.root = root_node

    def add_left(self, parent, child):
        parent.left = child

    def add_right(self, parent, child):
        parent.right = child

    # def __repr__(self):
    #     st_tree = []
    #     root = self.root
    #     while root:
    #         st_tree.append(root.val)
    #         if root.left:
    #             st_tree.append(root.left)
    #
    #         if root.right:
    #             st_tree.append(root.right)


def printtree(root):
    if not root:
        return
    q = [root]
    while len(q) > 0:
        curr = q.pop(0)
        print(curr)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return


# printtree(a)
def recursive(root):
    if not root:
        return
    print(root.val)
    if root.left:
        recursive(root.left)
    if root.right:
        recursive(root.right)


# recursive(a)
#
# def iter(root):
#     if root:
#         q = [root]
#     while len  n(q) > 0:
#         cur = q.pop(0)
#         print(cur)
#         if cur.left:
#             q.append(cur.left)
#         if cur.right:
#             q.append(cur.right)
#     return


def search(root, num):
    if root:
        if root.val == num:
            return True
        if root.val < num:
            return search(root.right, num)
        else:
            return search(root.left, num)
    return False


def iterative_search(root, num):
    if root:
        q = [root]


# print(search(a, 0))
# print(search(a, 1))
# print(search(a, -2))
# print(search(a, 11))
# print(search(a, 6))
a = Node(7)
b = Node(5)
c = Node(9)
d = Node(1)
e = Node(6)
g = Node(8)
f = Node(10)

BT = BinaryTree(a)
BT.add_left(a, b)
BT.add_right(a, c)
BT.add_left(b, d)
BT.add_right(b, e)
BT.add_left(c, g)
BT.add_right(c, f)


def display(root, num):
    if root:
        if root.val == num:
            return True
        return display(root.right, num) or display(root.left, num)
    return False


print(display(a, 10))
print(display(a, 0))
print(display(a, 1))
print(display(a, 9))
print(display(a, 11))
print(display(a, 6))

BT = BinaryTree(a)
BT.add_left(a, b)
BT.add_right(a, c)
BT.add_left(b, d)
BT.add_left(d, g)
BT.add_left(g, f)


def depth(root, s=0):
    if root:
        return max(depth(root.left, s + 1), depth(root.right, s + 1))
    return s


print(depth(a))
