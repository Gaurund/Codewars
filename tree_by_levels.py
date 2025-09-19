import unittest


class NodeTestCase(unittest.TestCase):
    def test_tree_by_levels(self):
        # self.assertEqual(tree_by_levels(None), [])
        self.assertEqual(
            tree_by_levels(
                Node(
                    Node(None, Node(None, None, 4), 2),
                    Node(Node(None, None, 5), Node(None, None, 6), 3),
                    1,
                )
            ),
            [1, 2, 3, 4, 5, 6],
        )


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node):
    result = list()
    queue = [node]
    while queue:
        n = queue.pop(0)
        if n is not None:
            result.append(n.value)
            queue.append(n.left)
            queue.append(n.right)
    return result if not node is None else []

unittest.main()

