import array
from dataclasses import dataclass
from typing import Tuple, List, Set


@dataclass
class Trail:
    """
    This is a simple wrapper class for the trail's underlying array.
    Implemented so we can protect the trail from edits by any walkers.
    Think of this class as the NPS ;)
    """
    _data: List[List[int]]  # TODO: optimize into memorymap?

    def __iter__(self):
        return iter(self._data)
    
    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: int) -> int:
        # TODO: Make items accessible by tuple as well
        return self._data[key]
    
    def __setitem__(self, *args):
        raise ValueError("Leave no trace! (Editing the trail is not allowed.)")


@dataclass
class Hiker:
    trail: Trail
    start_pos:Tuple[int, int]

    def can_reach(self, start: Tuple[int, int], end: Tuple[int, int]):
        # first make sure the destination is in bounds
        if end[0] < 0 or end[0] >= len(self.trail):
            return False
        elif end[1] < 0 or end[1] >= len(self.trail[0]):
            return False
        # If so, check the slope
        return True if abs(self.trail[start[0]][start[1]] - self.trail[end[0]][end[1]]) <= 1 else False
    
    def start(self) -> int:
        """
        This starts the traversal from root node.
        """
        return self.walk(self.start_pos, set())

    def walk(self, pos: Tuple[int, int], visited: Set[Tuple[int, int]]) -> int:
        """
        Use this to perform DFS for 9s. We want to gather a score for the trail.
        The number of 9s reachable from this trailhead is this trailhead's score.
        You may only walk up or down an incline of slope = 1.
        """
        # TODO: optimize by caching the score from each point encountered in the graph, to avoid recalculating
        # reaching multiple 9s on the same trail is a bit of a tough case
        # if we hit 9, we have to keep walking if possible, but the score should be increased by 1
        # base case, can't walk any more, return 1 if 9, 0 if not

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        next_tiles = [(y, x) for y, x in [(pos[0] + dy, pos[1] + dx) for dx, dy in directions]
                      if (y, x) not in visited and self.can_reach(pos, (y, x))]
        own_score: int = 1 if self.trail[pos[0]][pos[1]] == 9 else 0
        visited.add(pos)
        return sum([self.walk(n, visited) for n in next_tiles]) + own_score


def get_total_score(trail: Trail) -> int:
    total_score: int = 0
    for row in range(len(trail)):
        for col in range(len(trail[0])):
            if trail[row][col] == 0:
                hiker = Hiker(trail, (row, col))
                total_score += hiker.start()
    return total_score

if __name__ == "__main__":
    raw_trail: List[List[int]] = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            new_row: List[int] = []
            for c in line:
                if c != "\n":
                    new_row.append(int(c))
            raw_trail.append(new_row)
    trail = Trail(raw_trail)
    score: int = get_total_score(trail)
    print(score)
