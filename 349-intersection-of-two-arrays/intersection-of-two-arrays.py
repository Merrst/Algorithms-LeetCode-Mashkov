class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Преобразуем первый массив в Hash Set для быстрого поиска O(1)
        # Это также автоматически удалит дубликаты из nums1
        set1 = set(nums1)
        res = []
        
        # Превращаем второй массив в множество, чтобы брать только уникальные числа
        set2 = set(nums2)
        
        # Проходим по одному из множеств и проверяем наличие во втором
        for n in set1:
            if n in set2:
                res.append(n)
        
        return res