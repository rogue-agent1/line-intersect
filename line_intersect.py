#!/usr/bin/env python3
"""Line segment intersection detection and point computation."""
import sys

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def on_segment(p, q, r):
    return min(p[0],r[0]) <= q[0] <= max(p[0],r[0]) and min(p[1],r[1]) <= q[1] <= max(p[1],r[1])

def segments_intersect(p1, p2, p3, p4):
    d1 = cross(p3, p4, p1); d2 = cross(p3, p4, p2)
    d3 = cross(p1, p2, p3); d4 = cross(p1, p2, p4)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)): return True
    if d1 == 0 and on_segment(p3, p1, p4): return True
    if d2 == 0 and on_segment(p3, p2, p4): return True
    if d3 == 0 and on_segment(p1, p3, p2): return True
    if d4 == 0 and on_segment(p1, p4, p2): return True
    return False

def intersection_point(p1, p2, p3, p4):
    x1,y1 = p1; x2,y2 = p2; x3,y3 = p3; x4,y4 = p4
    denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(denom) < 1e-10: return None
    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/denom
    return (x1+t*(x2-x1), y1+t*(y2-y1))

def main():
    tests = [((0,0),(4,4),(0,4),(4,0)), ((0,0),(2,2),(3,3),(5,5)), ((0,0),(2,0),(1,-1),(1,1))]
    for p1,p2,p3,p4 in tests:
        hit = segments_intersect(p1,p2,p3,p4)
        pt = intersection_point(p1,p2,p3,p4) if hit else None
        print(f"{p1}-{p2} x {p3}-{p4}: {hit}" + (f" at {pt}" if pt else ""))

if __name__ == "__main__": main()
