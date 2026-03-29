#!/usr/bin/env python3
"""Line/segment intersection. Zero dependencies."""
import math

def line_intersection(p1, p2, p3, p4):
    x1,y1=p1; x2,y2=p2; x3,y3=p3; x4,y4=p4
    denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(denom) < 1e-10: return None
    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/denom
    return (x1+t*(x2-x1), y1+t*(y2-y1))

def segment_intersection(p1, p2, p3, p4):
    x1,y1=p1; x2,y2=p2; x3,y3=p3; x4,y4=p4
    denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(denom) < 1e-10: return None
    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/denom
    u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1+t*(x2-x1), y1+t*(y2-y1))
    return None

def point_to_line_dist(point, line_start, line_end):
    px,py=point; x1,y1=line_start; x2,y2=line_end
    dx,dy = x2-x1, y2-y1
    if dx==0 and dy==0: return math.hypot(px-x1, py-y1)
    t = max(0, min(1, ((px-x1)*dx+(py-y1)*dy)/(dx*dx+dy*dy)))
    return math.hypot(px-(x1+t*dx), py-(y1+t*dy))

def segments_intersect(p1, p2, p3, p4):
    return segment_intersection(p1, p2, p3, p4) is not None

if __name__ == "__main__":
    p = line_intersection((0,0),(1,1),(0,1),(1,0))
    print(f"Intersection: {p}")
