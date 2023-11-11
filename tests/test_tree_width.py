import pytest
from questions.tree_width import tree_width

@pytest.mark.parametrize("edges, expected", [
    ([[0, 1], [0, 2]], 2),
    ([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]], 4),
    ([], 0),  # No edges, single node tree
    ([[0, 1]], 1),  # A single edge
    ([[1, 0]], 1),  # Same as above, different direction (shouldn't matter in undirected graph)

    # Linear trees (chain like)
    ([[i, i+1] for i in range(99)], 99),  # Linear tree with 100 nodes
    ([[i, i+1] for i in range(999)], 999),  # Linear tree with 1000 nodes

    # Star shaped trees (one central node with all others connected to it)
    ([[0, i] for i in range(1, 100)], 2),  # Central node with 99 leaves
    ([[0, i] for i in range(1, 1000)], 2),  # Central node with 999 leaves

    ([[0, 1]] + [[i, i+1] for i in range(1, 499)] + [[1, 500]], 499),
    
    # Random large tree by connecting edges in a zig-zag pattern
    ([[i, i + (-1)**i] for i in range(1, 1000)], 1),  # Nodes connected in a zig-zag pattern
])

def test_tree_width(edges, expected):
    assert tree_width(edges) == expected
