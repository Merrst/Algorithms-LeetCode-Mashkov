class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # начинаем с начала списка
        left = 0
        
        # заканчиваем на последнем элементе
        right = len(nums) - 1

        # пока есть где искать
        while left <= right:
            
            # находим середину
            mid = (left + right) // 2

            # если нашли число
            if nums[mid] == target:
                return mid  # возвращаем его индекс
            
            # если число меньше нужного
            elif nums[mid] < target:
                # идем вправо
                left = mid + 1
            else:
                # идем влево
                right = mid - 1

        # если число не нашли,
        # left покажет место, куда его нужно вставить
        return left
