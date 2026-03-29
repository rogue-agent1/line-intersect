from line_intersect import line_intersection, segment_intersection, point_to_line_dist, segments_intersect
p = line_intersection((0,0),(1,1),(0,1),(1,0))
assert abs(p[0]-0.5)<0.01 and abs(p[1]-0.5)<0.01
assert line_intersection((0,0),(1,0),(0,1),(1,1)) is None  # parallel
s = segment_intersection((0,0),(1,1),(0,1),(1,0))
assert s is not None
assert segment_intersection((0,0),(0.4,0.4),(0.6,0.6),(1,1)) is None
d = point_to_line_dist((0,1),(0,0),(1,0))
assert abs(d-1.0)<0.01
assert segments_intersect((0,0),(1,1),(0,1),(1,0))
print("line_intersect tests passed")
