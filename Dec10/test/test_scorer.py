from trail_walker.scorer import Hiker, Trail, get_total_score

def test_single_trailhead():
    trail = Trail(
        [
            [0, 1, 2, 3],
            [9, 8, 5, 4],
            [9, 7, 6, 6],
        ]
    )
    total_score: int = get_total_score(trail)
    assert total_score == 2, "The hiker should have summited twice!"


def test_multi_trailhead():
    trail = Trail(
        [
            [0, 1, 2, 3],
            [9, 8, 5, 4],
            [9, 7, 6, 6],
            [8, 1, 6, 5],
            [0, 1, 3, 4],
            [0, 1, 2, 6],
        ]
    )
    total_score: int = get_total_score(trail)
    assert total_score == 6, "There were 3 trailheads, all reaching the same two summits."