import random

from intervaltree import IntervalTree


def test_adding_speed():
    base_tree = IntervalTree()
    l_bound = 0
    u_bound = 10000
    random.seed(10)
    for i in range(1000000):
        start = random.randint(l_bound, u_bound - 1)
        end = random.randint(start + 1, u_bound)
        base_tree.addi(start, end)
