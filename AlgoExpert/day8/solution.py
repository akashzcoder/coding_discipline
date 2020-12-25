from collections import defaultdict
from typing import TypeVar, List, Dict, Tuple, Iterator

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

from queue import *


Location = TypeVar('Location')


class Graph(Protocol):
    def neighbors(self, id: Location) -> List[Location]: pass


class SimpleGraph(Graph):
    def __init__(self):
        self.edges: Dict[Location, List[Location]] = {}

    def neighbors(self, id: Location) -> List[Location]:
        return self.edges[id]


example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': [],
}


def breadth_first_search(graph: Graph, start: Location):
    # print out what we find
    # Queue api: put, empty, ...
    frontier = Queue()
    reached = defaultdict(bool)
    frontier.put(start)
    while not frontier.empty():
        ele = frontier.get()
        reached[ele] = True
        print(f"Visiting {ele}")
        for edge in graph.neighbors(ele):
            if reached[edge] is False:
                frontier.put(edge)



print('Reachable from A:')
breadth_first_search(example_graph, 'A')
print('Reachable from E:')
breadth_first_search(example_graph, 'E')
