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


def walk(node: Node):
    if node is None:
        return ()
    node_list = [node.value, walk(node.left), walk(node.right)]
    return node_list



def tree_by_levels(node: Node):
    node_list = walk(node)
    rec_print(node_list)
    return node_list
    
def rec_print(node_list):
    if isinstance(node_list, int):
        print(node_list, end=" > ")
    else:
        for l in node_list:
            rec_print(l)

# unittest.main()

t = tree_by_levels(
                Node(
                    Node(None, Node(None, None, 4), 2),
                    Node(Node(None, None, 5), Node(None, None, 6), 3),
                    1,
                )
            )

print(t)
