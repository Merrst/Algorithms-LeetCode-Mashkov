from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Подсчитываем частоту каждого числа
        count = Counter(nums)
        
        # Создаем кучу для хранения k самых частых элементов
        heap = []
        
        # Проходим по всем числам и их частотам
        for num, freq in count.items():
            # Добавляем пару (частота, число) в кучу
            heapq.heappush(heap, (freq, num))
            
            # Если куча больше k, удаляем элемент с наименьшей частотой
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Извлекаем только числа из кучи
        return [num for freq, num in heap]