from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            # Добавляем текущий элемент
            heapq.heappush(heap, num)
            
            # Если куча выросла больше k, удаляем наименьший
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Верхушка кучи — k-й по величине элемент
        return heap[0]