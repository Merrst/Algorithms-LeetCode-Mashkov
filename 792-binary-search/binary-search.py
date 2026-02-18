class Solution:
    def search(self, nums: list[int], target: int):
        # начинаем поиск с самого начала списка
        left = 0
        
        # и до самого конца списка
        right = len(nums) - 1

        # пока есть где искать
        while left <= right:
            
            # берем число посередине
            mid = (left + right) // 2
            
            # если нашли нужное число
            if nums[mid] == target:
                return mid  # возвращаем его индекс
            
            # если число меньше нужного
            elif nums[mid] < target:
                # ищем правее
                left = mid + 1
            
            # если число больше нужного
            else:
                # ищем левее
                right = mid - 1
                
        # если число так и не нашли
        return -1
