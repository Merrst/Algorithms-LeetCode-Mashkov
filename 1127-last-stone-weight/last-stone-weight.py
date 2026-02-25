from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # В Python heapq - минимальная куча, поэтому храним отрицательные значения
        # чтобы имитировать максимальную кучу (самые тяжелые камни наверху)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)  # превращаем список в кучу за O(n)
        
        # Пока в куче больше одного камня
        while len(max_heap) > 1:
            # Берем два самых тяжелых камня (наибольшие числа, наименьшие отрицательные)
            y = -heapq.heappop(max_heap)  # самый тяжелый
            x = -heapq.heappop(max_heap)  # второй по тяжести
            
            # Если камни не равны, кладем обратно разницу
            if x != y:
                heapq.heappush(max_heap, -(y - x))
        
        # Если камней не осталось, возвращаем 0, иначе вес последнего камня
        return -max_heap[0] if max_heap else 0