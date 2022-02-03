from node import Node

visited = set()

def breadth_first_search(node: Node) -> Node:
    if node.id in visited:
        return
    
    visited.add(node.id)

    if len(node.neighbors) == 0:
        return

    for n in node.neighbors:
        breadth_first_search(n)


if __name__ == '__main__':
    n1 = Node(0, 0, set())
    n2 = Node(1, 1, set())
    n3 = Node(2, 2, {n1, n2})
    n4 = Node(3, 3, {n3, n2})
    breadth_first_search(n4)
    print(visited)