from intervaltree import IntervalTree, Interval


def test_search_method_s1():
    ### scenario 1
    # search for booking that only crosses v1 but not the intervals for v2
    v1 = Interval(0, 10, data=0)
    v2 = [Interval(0, 4, data=1), Interval(6, 10, data=1)]
    v2.append(v1)
    avail_tree = IntervalTree(v2)
    search_result = avail_tree.search_for_period_that_envelopes_range(3, 7)
    assert v1 in search_result and v2[0] not in search_result


def test_search_method_s2():
    ### scenario 2
    # search for booking that is equal to v1
    v1 = Interval(0, 10, data=0)
    v2 = [Interval(0, 4, data=1), Interval(6, 10, data=1)]
    v2.append(v1)
    avail_tree = IntervalTree(v2)
    search_result = avail_tree.search_for_period_that_envelopes_range(0, 10)
    assert v1 in search_result and v2[0] not in search_result


def test_chop_method_scenario1():
    ### scenario 1
    ###  We want to make sure we only chop the period of availability for v1
    v1 = Interval(0, 10, data=0)
    v2 = [Interval(0, 4, data=1), Interval(6, 10, data=1)]
    v2.append(v1)
    avail_tree = IntervalTree(v2)
    ### example booking
    avail_tree.chop_intervals_that_envelope_range(3, 7)
    assert avail_tree == IntervalTree(
        [Interval(0, 3, data=0), Interval(7, 10, data=0), Interval(0, 4, data=1), Interval(6, 10, data=1)])


def test_chop_method_scenario2():
    ### scenario 2
    ###  we want to make sure that we completely removea period that is exactly the same as the search
    v1 = Interval(0, 10, data=0)
    v2 = [Interval(0, 4, data=1), Interval(6, 10, data=1)]
    v2.append(v1)
    avail_tree = IntervalTree(v2)
    ### example booking
    avail_tree.chop_intervals_that_envelope_range(0, 10)
    assert avail_tree == IntervalTree(
        [Interval(0, 4, data=1), Interval(6, 10, data=1)])


def test_chop_method_w_criteria():
    ### scenario 3
    ### we want to only chop one period and not both
    v1 = [Interval(0, 10, data=0)]
    v2 = [Interval(0, 10, data=1)]
    v3 = [Interval(0, 4, data=2), Interval(6, 10, data=2)]
    intervals = sum((v1, v2, v3), [])
    avail_tree = IntervalTree(intervals)
    ### example booking for v1
    avail_tree.chop_intervals_that_envelope_range(3, 7, criteria=0)
    assert avail_tree == IntervalTree(
        [Interval(0, 3, data=0),
         Interval(7, 10, data=0),
         Interval(0, 10, data=1),
         Interval(0, 4, data=2),
         Interval(6, 10, data=2)])


def test_chop_method_w_limit():
    ### scenario 3
    ### we want to only chop one period and not both
    v1 = [Interval(0, 10, data=0)]
    v2 = [Interval(0, 10, data=1)]
    v3 = [Interval(0, 4, data=2), Interval(6, 10, data=2)]
    intervals = sum((v1, v2, v3), [])
    avail_tree = IntervalTree(intervals)
    ### example booking for v1
    avail_tree.chop_intervals_that_envelope_range(3, 7, limit=1)
    assert len(avail_tree.items()) == 5