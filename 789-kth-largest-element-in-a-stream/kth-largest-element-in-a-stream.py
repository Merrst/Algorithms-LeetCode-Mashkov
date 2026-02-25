from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)  # используем add для добавления начальных чисел
    
    def add(self, val: int) -> int:
        # Добавляем новое число в кучу
        heapq.heappush(self.heap, val)
        
        # Если куча стала больше k, удаляем самый маленький элемент
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # На вершине кучи - k-й по величине элемент
        return self.heap[0]