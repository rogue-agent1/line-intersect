#!/usr/bin/env python3
"""line_intersect: Line segment intersection detection."""
import sys

def ccw(A, B, C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def segments_intersect(A, B, C, D):
    if ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D):
        return True
    return False

def intersection_point(p1, p2, p3, p4):
    x1,y1 = p1; x2,y2 = p2; x3,y3 = p3; x4,y4 = p4
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(denom) < 1e-10: return None
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
    u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        x = x1 + t*(x2-x1)
        y = y1 + t*(y2-y1)
        return (x, y)
    return None

def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj-xi)*(y-yi)/(yj-yi)+xi):
            inside = not inside
        j = i
    return inside

def polygon_area(polygon):
    n = len(polygon)
    a = sum(polygon[i][0]*polygon[(i+1)%n][1] - polygon[(i+1)%n][0]*polygon[i][1] for i in range(n))
    return abs(a) / 2

def test():
    # Crossing segments
    assert segments_intersect((0,0),(2,2),(0,2),(2,0))
    assert not segments_intersect((0,0),(1,1),(2,2),(3,3))
    # Intersection point
    pt = intersection_point((0,0),(2,2),(0,2),(2,0))
    assert pt is not None
    assert abs(pt[0] - 1.0) < 0.001
    assert abs(pt[1] - 1.0) < 0.001
    # Parallel
    assert intersection_point((0,0),(1,0),(0,1),(1,1)) is None
    # Point in polygon
    square = [(0,0),(4,0),(4,4),(0,4)]
    assert point_in_polygon((2,2), square)
    assert not point_in_polygon((5,5), square)
    assert not point_in_polygon((-1,2), square)
    # Polygon area
    assert abs(polygon_area(square) - 16.0) < 0.001
    tri = [(0,0),(3,0),(0,4)]
    assert abs(polygon_area(tri) - 6.0) < 0.001
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Usage: line_intersect.py test")
