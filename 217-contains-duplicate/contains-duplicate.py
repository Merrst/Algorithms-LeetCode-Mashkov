class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Инициализируем хэш-таблицу (множество)
        # В Python set реализован через хэш-таблицу для быстрого поиска
        seen = set()
        
        for n in nums:
            # Если число уже есть в множестве, значит найден дубликат
            # Поиск в хэш-таблице занимает O(1)
            if n in seen:
                return True
            
            # Если числа нет, добавляем его в множество
            seen.add(n)
            
        # Если прошли весь массив и не нашли совпадений
        return False