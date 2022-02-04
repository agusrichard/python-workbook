from node import Node
from queuee import Queue

visited = set()
q = Queue()

def breadth_first_search(node: Node) -> Node:
    visited.add(node.id)
    for n in node.neighbors:
        if n in q or n.id in visited:
            continue
        q.enqueue(n)

    if len(q) == 0 and len(visited) != 0:
        return

    return breadth_first_search(q.dequeue())


if __name__ == '__main__':
    n0 = Node(0, 0, set())
    n1 = Node(1, 1, set())
    n2 = Node(2, 2, set())
    n3 = Node(3, 3, set())
    n4 = Node(4, 4, set())
    n5 = Node(5, 5, set())
    n6 = Node(6, 6, set())

    n0.add_nodes(n2)
    n1.add_nodes(n2, n3, n6)
    n2.add_nodes(n1, n3, n4, n0)
    n3.add_nodes(n1, n2, n4, n5)
    n4.add_nodes(n2, n3, n5)
    n5.add_nodes(n3, n4, n6)
    n6.add_nodes(n5, n1)
    breadth_first_search(n0)
    print(visited)