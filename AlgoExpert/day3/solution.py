import heapq


def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    vertices = len(edges)
    pq = []
    dist = [float('inf') for _ in range(vertices)]
    heapq.heappush(pq, (0, start))
    visited = set()
    while len(pq) > 0:
        s_dist, start = heapq.heappop(pq)
        if dist[start] > s_dist:
            dist[start] = s_dist
        if start not in visited:
            for dest, dest_dist in edges[start]:
                new_dist = s_dist + dest_dist
                heapq.heappush(pq, (new_dist, dest))
        visited.add(start)

    return [i if i != float('inf') else -1 for i in dist]
