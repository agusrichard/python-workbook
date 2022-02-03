from node import Node
from queuee import Queue

visited = set()
q = Queue()

def breadth_first_search(node: Node) -> Node:
    if len(q) == 0 and len(visited) != 0:
        return

    visited.add(node.id)
    for n in node.neighbors:
        if n in q and n.id in visited:
            continue
        q.enqueue(n)

    return breadth_first_search(q.dequeue())


if __name__ == '__main__':
    n1 = Node(0, 0, set())
    n2 = Node(1, 1, set())
    n3 = Node(2, 2, {n1, n2})
    n4 = Node(3, 3, {n3, n2})
    breadth_first_search(n4)
    print(visited)