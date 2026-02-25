from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Создаем кучу для хранения k ближайших точек
        heap = []
        
        # Проходим по всем точкам
        for x, y in points:
            # Вычисляем расстояние до начала координат (без квадратного корня для экономии)
            dist = x*x + y*y
            # Добавляем в кучу пару (расстояние, точка)
            # Используем отрицательное расстояние для максимальной кучи
            heapq.heappush(heap, (-dist, [x, y]))
            
            # Если куча больше k, удаляем точку с наибольшим расстоянием
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Извлекаем только точки из кучи
        return [point for dist, point in heap]