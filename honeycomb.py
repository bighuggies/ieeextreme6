#!/usr/bin/env python

import sys
import itertools

from collections import defaultdict

line = sys.stdin.readline().strip()
source, dest = line.split(',')
source = tuple(reversed([int(j) for j in source.split('.')]))
dest = tuple(reversed([int(j) for j in dest.split('.')]))

hexagons = {}
vertices = []
edges = defaultdict(set)

for x in range(1, 3):
    for y in range(1, 3):
        offset = x % 2 == 0

        c1 = (x,        (y * 2 + offset))           # top left
        c2 = ((x + 1),  (y * 2 + offset))           # top right
        c3 = ((x + 1),  (y * 2 + 1 + offset))       # middle right
        c4 = ((x + 1),  (y * 2 + 2 + offset))       # bottom right
        c5 = (x,        (y * 2 + 2 + offset))       # bottom left
        c6 = (x,        (y * 2 + 1 + offset))       # middle left

        hexagon = [c1, c2, c3, c4, c5, c6]

        vertices.extend(hexagon)
        hexagons[x, y] = hexagon

        edges[c1].add(c2)
        edges[c2].add(c1)

        edges[c2].add(c3)
        edges[c3].add(c2)

        edges[c3].add(c4)
        edges[c4].add(c3)

        edges[c4].add(c5)
        edges[c5].add(c4)

        edges[c5].add(c6)
        edges[c6].add(c5)

        edges[c6].add(c1)
        edges[c1].add(c6)

oo = float('inf')


def const(x):
    return lambda: x


def dijkstra(vertices, edges, start, end):
    dist = defaultdict(const(oo))
    dist[start] = 0

    q = vertices[:]

    while q:
        u, _ = min([(n, d) for n, d
                    in dist.iteritems() if n in q], key=lambda x: x[1])
        if u == end:
            break

        q.remove(u)

        if dist[u] == oo:
            break

        for v in edges[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt

    return dist[end]


d = min(dijkstra(vertices, edges, start, end) for start, end
        in itertools.product(
            hexagons[source],
            hexagons[dest])
        )

print(0 if source == dest else (d + 2) * 5)
