import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Построение списка смежности: узел -> список (сосед, вес)
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
            
        # Приоритетная очередь для хранения (время, узел)
        # Начинаем со стартового узла k с временем 0
        min_heap = [(0, k)]
        
        # Словарь для хранения кратчайшего времени до каждого узла
        visited = {}
        
        while min_heap:
            current_time, u = heapq.heappop(min_heap)
            
            # Если узел уже посещен с меньшим временем, пропускаем его
            if u in visited:
                continue
            
            # Фиксируем минимальное время для текущего узла
            visited[u] = current_time
            
            # Обход всех соседей текущего узла
            if u in graph:
                for v, travel_time in graph[u]:
                    if v not in visited:
                        # Добавляем соседа в кучу с обновленным суммарным временем
                        heapq.heappush(min_heap, (current_time + travel_time, v))
        
        # Если посещены все n узлов, возвращаем максимальное время из visited
        # В противном случае возвращаем -1
        if len(visited) == n:
            return max(visited.values())
        else:
            return -1