class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        def get_shortest_paths(start):
            distances = {i: float('inf') for i in range(1, n + 1)}
            distances[start] = 0
            min_heap = [(0, start)]

            while min_heap:
                curr_distance, curr_node = heapq.heappop(min_heap)

                if curr_distance > distances[curr_node]:
                    continue
                
                for neighbour, weight in graph[curr_node]:
                    distance = curr_distance + weight
                
                    if distance < distances[neighbour]:
                        distances[neighbour] = distance

                        heapq.heappush(min_heap, (distance, neighbour))

            return distances
        
        final_distances = get_shortest_paths(k)
        max_time = max(final_distances.values())
        return max_time if max_time < float('inf') else -1