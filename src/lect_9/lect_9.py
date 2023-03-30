class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"{self.val}"


def ancestor(node, parent):
    return parent.left == node or parent.right == node


class BinTree:
    def __init__(self, root):
        self.root = root

    def search_node(self, node, root=None):
        if not root:
            root = self.root
        if root.val == node.val:
            return root
        if root.left:
            res = self.search_node(node, root.left)
            if res:
                return res
        if root.right:
            res2 = self.search_node(node, root.right)
            if res2:
                return res2
        return None

    def add_left(self, parent, child):
        parent.left = child
        # parent_tree = self.search_node(parent)
        # if parent_tree:
        #     parent_tree.left = child
        #     child.parent = parent_tree
        # else:
        #     raise Exception("Parent node does not exist in tree")

    def add_right(self, parent, child):
        parent.right = child
        # parent_tree = self.search_node(parent)
        # if parent_tree:
        #     parent_tree.right = child
        #     child.parent = parent_tree
        # else:
        #     raise Exception("Parent node does not exist in tree")

    def isroot(self, node):
        return self.root.val == node.val

    # def isleaf(self, node):
    #     return not node.left and not node.right
    #     # node_tree = self.search_node(node)
    #     # if node_tree:
    #     #     if not node_tree.left and not node_tree.right:
    #     #         return True
    #     #     else:
    #     #         return False
    #     # else:
    #     #     raise Exception("Parent node does not exist in tree")
    #
    #
    #
    # def find_depth(self, node, s=0, root=None):
    #     if not root:
    #         root = self.root
    #     if root.val == node.val:
    #         return s
    #     if root.left:
    #         res = self.find_depth(node, s + 1, root.left)
    #         if res:
    #             return res
    #     if root.right:
    #         res = self.find_depth(node, s + 1, root.right)
    #         if res:
    #             return res
    #     return None

    # def find_height(self, node, s=0):
    #     if not node.left and node.right:
    #         return s
    #     if node.left:
    #         res = self.find_height(node.left, s + 1)
    #     else:
    #         res = s
    #     if node.right:
    #         res1 = self.find_height(node.right, s + 1)
    #     else:
    #         res1 = s
    #     return max(res, res1)

    def __repr__(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        return ""

    def _display_aux(self, root=None):
        # No child.
        if not root:
            root = self.root
        if root.right is None and root.left is None:
            line = '%s' % root.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.right is None:
            lines, n, p, x = self._display_aux(root.left)
            s = '%s' % root.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.left is None:
            lines, n, p, x = self._display_aux(root.right)
            s = '%s' % root.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(root.left)
        right, m, q, y = self._display_aux(root.right)
        s = '%s' % root.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def bfs(root):
    if root:
        q = [root]
    while len(q) > 0:
        cur = q.pop(0)
        print(cur)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)


a = Node("/")
b = Node("*")
c = Node("+")
d = Node("5")
e = Node("3")
g = Node("3")
h = Node("2")
# i = Node(8)
# j = Node(9)
BT = BinTree(a)
BT.add_left(a, b)
BT.add_right(a, c)
BT.add_left(b, d)
BT.add_right(b, e)
BT.add_left(c, g)
BT.add_right(c, h)

print(BT)


# bfs(a)
def printPostorder(root):
    s = ""
    if root:
        s += (root.left.val)
        s += root.val
        s += (root.right.val)
    return s


charcom = "/+-*"


def computation(root=None):
    q = [root]
    while len(q) > 0:
        cur = q.pop(0)
        try:
            if isinstance(int(cur.left.val), int) and isinstance(int(cur.right.val), int):
                res = eval(printPostorder(cur))
                cur.val = str(res)
        except:

            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
    return eval(printPostorder(root))

def computationrecurse(root=None):
    if not root:
        return
    try:
        return eval(str(computationrecurse(root.left)) + root.val + str(computationrecurse(root.right)))
    except:
        return root.val


print(computationrecurse(a))
