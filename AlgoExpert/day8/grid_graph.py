from typing import Tuple, List, Iterator, Protocol

GridLocation = Tuple[int, int]  # represents the x, y location on the map


class Graph(Protocol):
    def neighbors(self, id: GridLocation) -> Iterator[Tuple[int, int]]: pass


# create a grid graph that has 3 attributes: 1. height, 2. width and 3. obstacles
class GridGraph(Graph):
    def __init__(self, height: int, width: int, obstacles: List[Tuple[int, int]]):
        self.width = width
        self.height = height
        self.walls = obstacles

    def _is_in_bounds(self, id: GridLocation):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def _is_passable(self, id: GridLocation):
        return id not in self.walls

    def neighbors(self, id: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
        x, y = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        within_bounds = filter(self._is_in_bounds, neighbors)
        valid_neighbors = filter(self._is_passable, within_bounds)
        return valid_neighbors


