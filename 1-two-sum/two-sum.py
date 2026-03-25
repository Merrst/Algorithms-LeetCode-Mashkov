class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Инициализируем хэш-таблицу (словарь)
        # Ключ: значение числа, Значение: индекс этого числа в массиве
        prev_map = {} 
        
        for i, n in enumerate(nums):
            # Вычисляем разницу, которую нам нужно найти
            diff = target - n
            
            # Если разница уже есть в нашей хэш-таблице, 
            # значит мы нашли пару, которая в сумме дает target
            if diff in prev_map:
                # Возвращаем индекс найденной разницы и текущий индекс
                return [prev_map[diff], i]
            
            # Если не нашли, сохраняем текущее число и его индекс в таблицу
            prev_map[n] = i
            
        return []