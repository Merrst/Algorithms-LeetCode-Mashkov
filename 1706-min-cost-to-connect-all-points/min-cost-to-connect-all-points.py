import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # Итоговая минимальная стоимость и счетчик присоединенных точек
        total_cost = 0
        edges_used = 0
        # Массив для отслеживания точек, уже включенных в дерево
        visited = [False] * n
        # Куча хранит пары: (расстояние, индекс_точки)
        # Начинаем с 0-й точки, расстояние до самой себя — 0
        min_heap = [(0, 0)]
        
        while edges_used < n:
            cost, curr_node = heapq.heappop(min_heap)
            
            # Если точка уже в дереве, пропускаем её, чтобы не было циклов
            if visited[curr_node]:
                continue
            
            # Включаем точку в остовное дерево
            visited[curr_node] = True
            total_cost += cost
            edges_used += 1
            
            # Проверяем все остальные точки и добавляем их в кучу
            for next_node in range(n):
                if not visited[next_node]:
                    # Вычисляем расстояние Манхэттена между текущей и следующей точкой
                    dist = abs(points[curr_node][0] - points[next_node][0]) + \
                           abs(points[curr_node][1] - points[next_node][1])
                    heapq.heappush(min_heap, (dist, next_node))
                    
        return total_cost