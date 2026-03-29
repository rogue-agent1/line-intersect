#!/usr/bin/env python3
"""line_intersect - Line segment intersection and sweep line algorithm."""
import sys

def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def segments_intersect(A, B, C, D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def intersection_point(p1, p2, p3, p4):
    x1,y1 = p1; x2,y2 = p2; x3,y3 = p3; x4,y4 = p4
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(denom) < 1e-12:
        return None
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
    x = x1 + t*(x2-x1)
    y = y1 + t*(y2-y1)
    u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x, y)
    return None

def find_all_intersections(segments):
    results = []
    n = len(segments)
    for i in range(n):
        for j in range(i+1, n):
            p = intersection_point(segments[i][0], segments[i][1], segments[j][0], segments[j][1])
            if p is not None:
                results.append((i, j, p))
    return results

def test():
    # crossing segments
    assert segments_intersect((0,0),(1,1),(0,1),(1,0))
    assert not segments_intersect((0,0),(1,0),(0,1),(1,1))
    # intersection point
    p = intersection_point((0,0),(1,1),(0,1),(1,0))
    assert p is not None
    assert abs(p[0] - 0.5) < 1e-9 and abs(p[1] - 0.5) < 1e-9
    # parallel
    assert intersection_point((0,0),(1,0),(0,1),(1,1)) is None
    # find all
    segs = [((0,0),(1,1)), ((0,1),(1,0)), ((0,0.5),(1,0.5))]
    ints = find_all_intersections(segs)
    assert len(ints) == 3  # all pairs intersect
    print("OK: line_intersect")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: line_intersect.py test")
